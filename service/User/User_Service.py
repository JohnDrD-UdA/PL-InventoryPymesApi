from sqlalchemy import or_
from config.config import conn
from models.User.User import User
from models.User.User_DTO import UserDTO

class UserService():    
    def getUsers(self):
        result=conn.execute(User.select())
        resultAsList=[r._asdict() for r in result]
        return resultAsList
    
    def createUsers(self,data: UserDTO):
        return conn.execute(User.insert().values(data.__dict__))
    
    def updateUsers(self,id:int,data:UserDTO):
        values= data.__dict__
        conn.execute(User.update().where(User.c.id == id).values(values))
        return values
    def deleteUsers(self,id:int):
        return conn.execute(User.delete().where(User.c.id == id))