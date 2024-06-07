from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String,Float,BigInteger
from config.config import Base

class Bills(Base):
    __tablename__='Bills'

    id= Column(Integer, primary_key=True)
    final_cost=Column(Float, nullable=False)
    date_created=Column(BigInteger, nullable=False)
    date_paid=Column(BigInteger, nullable=True)
    state=Column(String(20), nullable=False)
    client_id=Column(Integer, nullable=False)
    owner_id=Column(Integer, nullable=False)