from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from config.config import Base

class Units(Base):
    __tablename__='Units'

    id= Column(Integer, primary_key=True)
    name=Column(String(20), nullable=False,unique=True)
    state=Column(Boolean, nullable=False)