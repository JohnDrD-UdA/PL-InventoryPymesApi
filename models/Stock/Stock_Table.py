from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,Float
from config.config import Base

class Stocks(Base):
    __tablename__='Stocks'

    id= Column(Integer, primary_key=True)
    product_id=Column(Integer, nullable=False)
    location_id=Column(Integer, nullable=False)
    amount=Column(Float, nullable=False)