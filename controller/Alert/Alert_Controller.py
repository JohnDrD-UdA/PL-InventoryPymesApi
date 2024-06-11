from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from service.Alert.Alert_Service import AlertService


alertController= APIRouter()
service= AlertService()
TAG="Alerts"
@alertController.get("/alerts",dependencies=[Depends(validateToken)],tags=[TAG])
def getAlerts():
    return service.getAlerts()

@alertController.delete("/alerts/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteAlert(id: int):
    return service.deleteAlert(id)