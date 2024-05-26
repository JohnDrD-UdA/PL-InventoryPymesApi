from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from config.config import Base

class Alerts(Base):
    __tablename__='Alerts'
    
    id= Column(Integer, primary_key=True)
    msg=Column(String(100), nullable=False)
    date_created=Column(Integer, nullable=False)
    state=Column(Boolean, nullable=True)
    type_id=Column(Integer, nullable=False)