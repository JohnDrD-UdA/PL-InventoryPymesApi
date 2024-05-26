from config.config import session
from models.Location.Location import Locations
from models.Location.Location_DTO import locationDTO

class LocationService():    
    def getLocations(self):
        try:
            result= session.query(Locations).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createLocations(self,data: locationDTO):
        try:
            new_location= Locations(name=data.name, manager_id=data.manager_id, address=data.address, phone=data.phone)
            session.add(new_location)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
    def updateLocations(self,id:int,data:locationDTO):
        try:
            location= session.query(Locations).get(id)
            if location:
                location.name= data.name
                location.phone=data.phone
                location.address=data.address
                location.manager_id=data.mail
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def deleteLocations(self,id:int):
        try:
            location= session.query(Locations).get(id)
            if location:
                session.delete(location)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def getLocationById(seld,id:int):
        try:
            result= session.query(Locations).get(id)
            if result:
                return result
            return "404"
        except Exception as e:
            print(e)
            return "fail"