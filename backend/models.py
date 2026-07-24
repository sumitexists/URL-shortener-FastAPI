
from sqlmodel import SQLModel, Field


class UrlBase(SQLModel, table = True ):
    id : int = Field(default=None, primary_key=True)
    url : str = Field(unique=True)
    shortend_url : str = Field(default=None,unique=True)
