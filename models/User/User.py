from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.config import engine,meta_data

User= Table("User", meta_data, 
              Column("id",Integer, primary_key=True),
              Column("name",String(100), nullable=False),
              Column("phone",String(20), nullable=False),
              Column("address",String(50), nullable=False),
              Column("mail",String(50), nullable=False),
              Column("rol_id",Integer, nullable=True),
              )

meta_data.create_all(engine)