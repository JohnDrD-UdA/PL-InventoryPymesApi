from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from models.Unit.Unit_DTO import UnitDTO
from service.Unit.Unit_Service import UnitService


unitsController= APIRouter()
service= UnitService()
TAG="Units"
@unitsController.get("/units",dependencies=[Depends(validateToken)],tags=[TAG])
def getUnits():
    return service.getUnits()

@unitsController.get("/units/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def getUnitById(id:int):
    return service.getUnitById(id)

@unitsController.post("/units/create",dependencies=[Depends(validateToken)],tags=[TAG])
def createUnit(data: UnitDTO):
    return service.createUnits(data)

@unitsController.put("/units/update/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def updateUnit(id:int, data:UnitDTO):
    return service.updateUnits(id,data)

@unitsController.delete("/units/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteUnit(id: int):
    return service.deleteUnits(id)