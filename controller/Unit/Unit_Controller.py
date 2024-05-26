from fastapi import APIRouter
from models.Unit.Unit_DTO import UnitDTO
from service.Unit.Unit_Service import UnitService


unitsController= APIRouter()
service= UnitService()

@unitsController.get("/units")
def getUnits():
    return service.getUnits()

@unitsController.get("/units/{id}")
def getUnitById(id:int):
    return service.getUnitById(id)

@unitsController.post("/units/create")
def createUnit(data: UnitDTO):
    return service.createUnits(data)

@unitsController.put("/units/update/{id}")
def updateUnit(id:int, data:UnitDTO):
    return service.updateUnits(id,data)

@unitsController.delete("/units/{id}")
def deleteUnit(id: int):
    return service.deleteUnits(id)