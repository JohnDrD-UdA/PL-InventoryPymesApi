from fastapi import APIRouter
from models.Alert_Type.AlertType_DTO import AlertTypeDTO
from service.Alert_Type.Alert_Type_Service import AlertTypeService


alertTypeController= APIRouter()
service= AlertTypeService()

@alertTypeController.get("/alertTypes")
def getAlertTypes():
    return service.getAlertTypes()

@alertTypeController.get("/alertType/{id}")
def getAlertTypeById(id:int):
    return service.getAlertTypeById(id)

@alertTypeController.post("/alertTypes/create")
def createAlertType(data: AlertTypeDTO):
    return service.createAlertTypes(data)

@alertTypeController.put("/alertTypes/update/{id}")
def updateAlertType(id:int, data:AlertTypeDTO):
    return service.updateAlertTypes(id,data)

@alertTypeController.delete("/alertTypes/{id}")
def deleteAlertType(id: int):
    return service.deleteAlertTypes(id)