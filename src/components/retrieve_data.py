from src.models.retrieve_data_model.retrieve_data_request import RetrieveDataRequest
from sqlalchemy import select


class RetrieveData:
    def __init__(self, data: RetrieveDataRequest, session_local):
        """ Object to handle data retrieval
        Args:
            data (RetrievalDataRequest): Pydantic request object
            db: Database session. 
        """

        self.data = data
        self.db = db

    
    async def create_sql_query(self) -> None:
        with SessionLocal() as session:
            query = select([getattr(models.c, field) for field in request.fields]).where(
                models.c.modelName == request.modelName
            )

            for filter_item in request.filters:
                if filter_item.operator == "==":
                    query = query.where(getattr(models.c, filter_item.field) == filter_item.value)
                elif filter_item.operator == ">=":
                    query = query.where(getattr(models.c, filter_item.field) >= filter_item.value)
                elif filter_item.operator == "<=":
                    query = query.where(getattr(models.c, filter_item.field) <= filter_item.value)
                elif filter_item.operator == ">":
                    query = query.where(getattr(models.c, filter_item.field) > filter_item.value)
                elif filter_item.operator == "<":
                    query = query.where(getattr(models.c, filter_item.field) < filter_item.value)
                
            result = session.execute(query)
            data = [dict(row) for row in result]

    return {"data": data}


    async def get_result(self) -> dict:
        pass
    
    
        

    