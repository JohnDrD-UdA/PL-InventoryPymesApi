from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.config import engine,meta_data

Client= Table("Client", meta_data, 
              Column("id",Integer, primary_key=True),
              Column("name",String(100), nullable=False),
              Column("lastname",String(100), nullable=False),
              Column("phone",String(20), nullable=False),
              Column("age",Integer, nullable=False),
              Column("gender",String(20), nullable=False),
              )

meta_data.create_all(engine)