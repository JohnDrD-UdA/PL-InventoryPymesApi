from fastapi import APIRouter
from models.Bill_Item.BillItem_DTO import BillItemDTO
from service.Bill_Item.Billitem_Service import ItemService


itemsController= APIRouter()
service= ItemService()

@itemsController.get("/items")
def getItem():
    return service.getItem()

@itemsController.get("/items/{id}")
def getItemById(id:int):
    return service.getItemById(id)

@itemsController.post("/items/create")
def createItem(data: BillItemDTO):
    return service.createItem(data)

@itemsController.put("/items/update/{id}")
def updateItem(id:int, data:BillItemDTO):
    return service.updateItem(id,data)

@itemsController.delete("/items/{id}")
def deleteItem(id: int):
    return service.deleteItem(id)