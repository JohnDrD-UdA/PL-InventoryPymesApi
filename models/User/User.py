from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.config import Base

class Users(Base):
    __tablename__='Users'

    id= Column(Integer, primary_key=True)
    name=Column(String(100), nullable=False)
    phone=Column(String(20), nullable=False)
    address=Column(String(50), nullable=False)
    mail=Column(String(50), nullable=False)
    rol_id=Column(Integer, nullable=True)