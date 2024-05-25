from fastapi import APIRouter
from service.Location.Location_Service import LocationService
from typing import List
from models.Location.Location_DTO import locationDTO

locationController= APIRouter()
service= LocationService()

@locationController.get("/location")
def getLocation():
    return service.getLocation()

@locationController.post("/location/create")
def createLocation(data: locationDTO):
    return service.createLocation(data)

@locationController.put("/location/update/{id}",response_model=locationDTO)
def updateLocation(id:int, data:locationDTO):
    return service.updateLocation(id,data)

@locationController.delete("/location/{id}")
def deleteLocation(id: int):
    return service.deleteLocation(id)