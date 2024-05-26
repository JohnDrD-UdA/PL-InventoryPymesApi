from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String,Float
from config.config import Base

class Products(Base):
    __tablename__='Products'

    id= Column(Integer, primary_key=True)
    name=Column(String(100), nullable=False)
    unit_cost=Column(Float, nullable=False)
    unit_id=Column(Integer, nullable=False)
    prov_id=Column(Integer, nullable=False)