from sqlalchemy import Column, Integer, String, DateTime, Text
from src.database.database import Base
from datetime import datetime

class Document(Base):
  __tablename__ = 'tabuser'
  
  id = Column(Integer(), primary_key=True)
  firstName = Column(String, index=True, nullable=False)
  lastName = Column(String, index=True, nullable=False)
  modelName = Column(String, index=True, nullable=False)
  createdAt = Column(DateTime(), default=datetime.now(), nullable=False, index=True)
  updatedAt = Column(DateTime(), nullable=True)

class User(Document):  
    pass
