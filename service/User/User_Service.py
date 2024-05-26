from config.config import session
from models.User.User import Users
from models.User.User_DTO import UserDTO

class UserService():    
    def getUsers(self):
        try:
            result= session.query(Users).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createUsers(self,data: UserDTO):
        try:
            new_user= Users(name=data.name, phone=data.phone, address=data.address, mail=data.mail,rol_id= data.rol_id)
            session.add(new_user)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
    def updateUsers(self,id:int,data:UserDTO):
        try:
            user= session.query(Users).get(id)
            if user:
                user.name= data.name
                user.phone=data.phone
                user.address=data.address
                user.mail=data.mail
                user.rol_id= data.rol_id
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def deleteUsers(self,id:int):
        try:
            user= session.query(Users).get(id)
            if user:
                session.delete(user)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def getUserById(seld,id:int):
        try:
            result= session.query(Users).get(id)
            if result:
                return result
            return "404"
        except Exception as e:
            print(e)
            return "fail"