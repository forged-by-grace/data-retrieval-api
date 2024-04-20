from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.configuration import ConfigurationManager


# Init config
config = ConfigurationManager()
database_config = config.get_database_config()

# Init the SQLite database url
SQLALCHEMY_DATABASE_URL = database_config.database_url

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a local session class instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# set the base class to be inherited by SQLALCHEMY models
Base = declarative_base()