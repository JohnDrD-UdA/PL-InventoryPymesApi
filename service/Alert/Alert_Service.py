from models.Alert.Alert import Alerts
from config.config import session


class AlertService():    
    def getAlerts(self):
        try:
            result= session.query(Alerts).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
        
    def deleteAlert(self,id:int):
        try:
            result= session.query(Alerts).get(id)
            if result:
                session.delete(result)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"