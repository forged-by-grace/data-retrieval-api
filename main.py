from src.config.configuration import ConfigurationManager
from src.utils import logger

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.hooks.hooks import (
    after_start_hooks, before_migrate_hooks, after_migrate_hooks,
    register_after_start, register_before_migrate, register_after_migrate
)

from src.models.user.user import User
from src.schemas.schema import UserCreate, User, RetrieveDataRequest
from src.database.database import SessionLocal, engine

from sqlalchemy.orm import Session

from src.controllers.controller import create_user_ctr, get_user_ctr, retrieve_data_ctr
from src.models.user import user

from typing import List


# Create tables if it does not exist
user.Base.metadata.create_all(bind=engine)


# SQLALCHEMY dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Load start-up configurations
config = ConfigurationManager()
app_config = config.get_app_config()
logger.info('App config files loaded successfully')


async def on_startup():
    logger.info('Starting data retrieval server...')
    logger.info('Running system hooks')
    # Run the system hooks
    await after_start_hooks("arg1", "arg2", kwarg1="kwarg1")
    await before_migrate_hooks("arg")
    await after_migrate_hooks()


async def on_shut_down():
    logger.info('Shutting down data retrieval  server')


# init app lifecyle
@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup()
    yield
    await on_shut_down()


# Init fastapi
app = FastAPI(    
    lifespan=lifespan,
    title=app_config.app_title,
    version=app_config.app_version,
    description=app_config.app_description,
    contact={
        'name': app_config.app_developer_name,
        'url': app_config.app_developer_repo_url,
        'email': app_config.app_developer_email
    }
)


# Set CORS
origins = ['*']


# add middleware
app.add_middleware(
    CORSMiddleware,    
    allow_origins=origins,
    allow_methods=['post', 'get'],
    allow_credentials=True,
    allow_headers=['application/json', 'authorization'],
)



@app.post('/retrieve_data/', response_model=List[User], response_model_exclude_none=True, response_model_exclude_unset=True)
async def retrieve_data(request: RetrieveDataRequest, db: Session = Depends(get_db)):
    return await retrieve_data_ctr(request=request, db=db)


@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return await create_user_ctr(user=user, db=db)


@app.get("/users/{user_id}", response_model=User, response_model_exclude_none=True, response_model_exclude_unset=True)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return await get_user_ctr(user_id=user_id, db=db)


if __name__ == '__main__':
    uvicorn.run(
        app_config.app_entry_point,
        port=app_config.app_port,
        reload=app_config.app_reload,
        host=app_config.app_host,
        lifespan=app_config.app_lifespan
    )