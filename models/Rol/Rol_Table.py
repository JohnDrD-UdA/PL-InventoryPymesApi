from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String,Float,Boolean
from config.config import Base

class Roles(Base):
    __tablename__='Roles'
    
    id= Column(Integer, primary_key=True)
    name=Column(String(20), nullable=False,unique=True)
    state=Column(Boolean, nullable=False)