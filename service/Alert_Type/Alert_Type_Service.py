from config.config import session
from models.Alert_Type.Alert_Type import AlertType
from models.Alert_Type.AlertType_DTO import AlertTypeDTO

class AlertTypeService():    
    def getAlertTypes(self):
        try:
            result= session.query(AlertType).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createAlertTypes(self,data: AlertTypeDTO):
        try:
            new_rol= AlertType(name=data.name, state=data.state)
            session.add(new_rol)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
    def updateAlertTypes(self,id:int,data:AlertTypeDTO):
        try:
            rol= session.query(AlertType).get(id)
            if rol:
                rol.state=data.state
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def deleteAlertTypes(self,id:int):
        try:
            rol= session.query(AlertType).get(id)
            if rol:
                session.delete(rol)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def getAlertTypeById(seld,id:int):
        try:
            result= session.query(AlertType).get(id)
            if result:
                return result
            return "404"
        except Exception as e:
            print(e)
            return "fail"