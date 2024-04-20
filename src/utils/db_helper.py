from sqlalchemy.orm import Session

from src.models.user.user import User
from src.schemas.schema import UserCreate, RetrieveDataRequest

from sqlalchemy import select
from fastapi import HTTPException, status

from src.utils import logger


async def create_user(db: Session, user: UserCreate):
    # Init sqlalchemy user model
    db_user = User(firstName=user.firstName.lower(), lastName=user.lastName.lower(), modelName=user.modelName.lower())
    
    # Commit to db
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


async def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
    

async def retrieve_data(db: Session, request: RetrieveDataRequest):
    try:
        # Select query
        query = select(*[getattr(User, field) if field != '*' else User for field in request.fields]).where(
            User.modelName == request.modelName.lower()
        )
            
        # Add filters
        for filter_item in request.filters:
            # Get Table column
            column = getattr(User, filter_item.field)

            # Get filter value
            filter_value = filter_item.value.lower() if type(filter_item.value) == str else filter_item.value
            
            if filter_item.operator == '==':
                query = query.where(column == filter_value)
            elif filter_item.operator == '>=':
                query = query.where(column >= filter_value)
            elif filter_item.operator == '<=':
                query = query.where(column <= filter_value)
            elif filter_item.operator == '>':
                query = query.where(column > filter_value)
            elif filter_item.operator == '<':
                query = query.where(column < filter_value)
            else:
                logger.warning(f'Invalid filter operator: {filter_item.operator}')
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'Invalid filter operator: {filter_item.operator}'
                )
        
        # Execute query
        result = db.execute(query).fetchall()

        # Parse the result
        data = [convert_row_to_dict(row, request.fields) if '*' not in request.fields else row[0] for row in result]
        return data
    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="One or more request values are invalid"
        )



def convert_row_to_dict(rows, fields):
    result = {}
    for i in range(len(rows)):
        result[fields[i]] = rows[i]
    return result