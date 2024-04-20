"""
    This contains pydantic models also called schemas for creating and reading data.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime


class UserCreate(BaseModel):
    modelName: str = Field(description='Name of the model', examples=['User'])
    firstName: str = Field(description='Firstname of the user',examples=['John'])
    lastName: str = Field(description='Lastname of the user', examples=['Doe'])


class User(BaseModel):
    id: Optional[int] = Field(default=None, description='ID of the user.', examples=[1])
    modelName: Optional[str] = Field(default=None, description='Name of the model', examples=['User'])
    firstName: Optional[str] = Field(default=None, description='Firstname of the user',examples=['John'])
    lastName: Optional[str] = Field(default=None, description='Lastname of the user', examples=['Doe'])
    createdAt: Optional[datetime] = Field(default=None, description='Datetime when the user was created.')
    updatedAt: Optional[datetime] = Field(default=None, description='Datetime of last update', ) 
    
    class Config:
        orm_mode = True


class Filter(BaseModel):
    field: str = Field(description="Database field to be queried", examples=['firstName', 'lastName'])
    operator: str = Field(description="Database operator", examples=['>=', '<=', '==', '>', '<'])
    value: str | int = Field(description="Value to be queried", examples=['John', '20-04-2023'])


class RetrieveDataRequest(BaseModel):
    modelName: str = Field(description="Name of the model.", examples=['User'])
    fields: List[str] = Field(description="Fields to retrieve", examples=[['*']])
    filters: List[Filter] = Field(description="Object specifying filter conditions")

