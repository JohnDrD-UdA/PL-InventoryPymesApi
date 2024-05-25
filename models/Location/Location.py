from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.config import engine,meta_data

Location= Table("Location", meta_data, 
              Column("id",Integer, primary_key=True),
              Column("name",String(100), nullable=False),
              Column("manager_id",Integer, nullable=True),
              Column("phone",String(20), nullable=False),
              Column("address",String(100), nullable=False),
              )

meta_data.create_all(engine)