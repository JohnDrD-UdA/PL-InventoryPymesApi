from fastapi import APIRouter
from models.clients import Client
from service.ClientService import ClientService
from typing import List
from models.client_model import clientDTO

clientController= APIRouter()
service= ClientService()

@clientController.get("/clients")
def getClients():
    return service.getClients()

@clientController.post("/client/create")
def createClient(data: clientDTO):
    return service.createClient(data)

@clientController.put("/client/update/{id}",response_model=clientDTO)
def updateClient(id:int, data:clientDTO):
    return service.updateClient(id,data)

@clientController.delete("/client/{id}")
def deleteClient(id: int):
    return service.deleteClient(id)