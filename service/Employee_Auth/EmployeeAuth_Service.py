from config.config import session
from models.Employee_Auth.EmployeeAuth import EmployeeAuth
from models.Employee_Auth.EmployeeAuth_DTO import EmployeeAuthDTO

class AuthService():    
    def createAuth(self,data: EmployeeAuthDTO):
        try:
            new_user= EmployeeAuth(userName=data.userName, last_login=data.last_login, state=data.state, user_id=data.user_id)
            session.add(new_user)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
        
    def deleteAuth(self,id:int):
        try:
            user= session.query(EmployeeAuth).get(id)
            if user:
                session.delete(user)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"