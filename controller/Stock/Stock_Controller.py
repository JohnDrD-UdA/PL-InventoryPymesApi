from fastapi import APIRouter
from models.Stock.Stock_DTO import StockDTO
from service.Stock.Stock_Service import StockService


stocksController= APIRouter()
service= StockService()

@stocksController.get("/stocks")
def getStocks():
    return service.getStocks()

@stocksController.get("/stocks/{id}")
def getStockById(id:int):
    return service.getStockById(id)

@stocksController.post("/stocks/create")
def createStock(data: StockDTO):
    return service.createStocks(data)

@stocksController.put("/stocks/update/{id}")
def updateStock(id:int, data:StockDTO):
    return service.updateStocks(id,data)

@stocksController.delete("/stocks/{id}")
def deleteStock(id: int):
    return service.deleteStocks(id)