from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from models.Alert_Type.AlertType_DTO import AlertTypeDTO
from service.Alert_Type.Alert_Type_Service import AlertTypeService


alertTypeController= APIRouter()
service= AlertTypeService()
TAG="Alert_Type"
@alertTypeController.get("/alertTypes",dependencies=[Depends(validateToken)],tags=[TAG])
def getAlertTypes():
    return service.getAlertTypes()

@alertTypeController.get("/alertType/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def getAlertTypeById(id:int):
    return service.getAlertTypeById(id)

@alertTypeController.post("/alertTypes/create",dependencies=[Depends(validateToken)],tags=[TAG])
def createAlertType(data: AlertTypeDTO):
    return service.createAlertTypes(data)

@alertTypeController.put("/alertTypes/update/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def updateAlertType(id:int, data:AlertTypeDTO):
    return service.updateAlertTypes(id,data)

@alertTypeController.delete("/alertTypes/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteAlertType(id: int):
    return service.deleteAlertTypes(id)