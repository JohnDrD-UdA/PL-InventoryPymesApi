from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.config import Base, engine

class Locations(Base):
    __tablename__='Locations'

    id= Column(Integer, primary_key=True)
    name=Column(String(100), nullable=False)
    manager_id=  Column(Integer, nullable=True)
    phone=Column(String(20), nullable=False)
    address= Column(String(100), nullable=False)