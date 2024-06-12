from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from service.Location.Location_Service import LocationService
from typing import List
from models.Location.Location_DTO import locationDTO

locationController= APIRouter()
service= LocationService()
TAG="Locations"
@locationController.get("/location",dependencies=[Depends(validateToken)],tags=[TAG])
def getLocation():
    return service.getLocations()

@locationController.post("/location/create",dependencies=[Depends(validateToken)],tags=[TAG])
def createLocation(data: locationDTO):
    return service.createLocations(data)

@locationController.put("/location/update/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def updateLocation(id:int, data:locationDTO):
    return service.updateLocations(id,data)

@locationController.delete("/location/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteLocation(id: int):
    return service.deleteLocations(id)