from sqlalchemy.orm import Session

from src.schemas.schema import UserCreate, User, RetrieveDataRequest
from src.utils.db_helper import create_user, get_user, retrieve_data


from fastapi import HTTPException, status


async def create_user_ctr(user: UserCreate, db: Session) -> User:
    return await create_user(user=user, db=db)


async def get_user_ctr(user_id: int, db: Session) -> User:
    user = await get_user(user_id=user_id, db=db)
    
    # Check if user exists
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id:{user_id} does not exist."
        )

    return user


async def retrieve_data_ctr(request: RetrieveDataRequest, db: Session):
    
    result = await retrieve_data(request=request, db=db)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No match was found for your request."
        )

    return result
    