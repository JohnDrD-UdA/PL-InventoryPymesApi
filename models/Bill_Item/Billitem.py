from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,Float
from config.config import Base

class Bill_Items(Base):
    __tablename__='Bill_Items'

    id= Column(Integer, primary_key=True)
    product_id=Column(Integer, nullable=False)
    bill_id=Column(Integer, nullable=False)
    ammount=Column(Float, nullable=False)