from config.config import session
from models.Rol.Rol_Table import Roles
from models.Rol.Rol_DTO import RolDTO

class RolService():    
    def getRoles(self):
        try:
            result= session.query(Roles).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createRoles(self,data: RolDTO):
        try:
            new_rol= Roles(name=data.name, state=data.state)
            session.add(new_rol)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
    def updateRoles(self,id:int,data:RolDTO):
        try:
            rol= session.query(Roles).get(id)
            if rol:
                rol.state=data.state
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def deleteRoles(self,id:int):
        try:
            rol= session.query(Roles).get(id)
            if rol:
                session.delete(rol)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def getRolById(seld,id:int):
        try:
            result= session.query(Roles).get(id)
            if result:
                return result
            return "404"
        except Exception as e:
            print(e)
            return "fail"