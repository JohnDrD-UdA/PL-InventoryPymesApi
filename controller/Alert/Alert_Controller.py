from fastapi import APIRouter
from service.Alert.Alert_Service import AlertService


alertController= APIRouter()
service= AlertService()

@alertController.get("/alerts")
def getAlerts():
    return service.getAlerts()

@alertController.delete("/alerts/{id}")
def deleteAlert(id: int):
    return service.deleteAlert(id)