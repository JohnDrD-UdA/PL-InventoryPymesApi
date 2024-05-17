from sqlalchemy import or_
from config.config import conn
from models.Location import Location_DTO
from models.Location.Location import Location

class LocationService():    
    def getLocation(self):
        result=conn.execute(Location.select())
        resultAsList=[r._asdict() for r in result]
        return resultAsList
    
    def createLocation(self,data: Location_DTO):
        return conn.execute(Location.insert().values(data.__dict__))
    
    def updateLocation(self,id:int,data:Location_DTO):
        values= data.__dict__
        print(values)
        conn.execute(Location.update().where(Location.c.id == id).values(values))
        return values
    def deleteLocation(self,id:int):
        return conn.execute(Location.delete().where(Location.c.id == id))