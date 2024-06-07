from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import BigInteger,String,Boolean,Integer
from config.config import Base

class EmployeeAuth(Base):
    __tablename__='Employee_Auth'
    
    id= Column(Integer, primary_key=True)
    user_name=Column(String(100), nullable=False,unique=True)
    password= Column(String(200), nullable=False)
    last_login=Column(BigInteger)
    state=Column(Boolean, nullable=False)
    user_id= Column(Integer,nullable=False)