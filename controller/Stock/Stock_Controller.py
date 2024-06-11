from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from models.Stock.Stock_DTO import StockDTO
from service.Stock.Stock_Service import StockService


stocksController= APIRouter()
service= StockService()
TAG="Stock"
@stocksController.get("/stocks",dependencies=[Depends(validateToken)],tags=[TAG])
def getStocks():
    return service.getStocks()

@stocksController.get("/stocks/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def getStockById(id:int):
    return service.getStockById(id)

@stocksController.post("/stocks/create",dependencies=[Depends(validateToken)],tags=[TAG])
def createStock(data: StockDTO):
    return service.createStocks(data)

@stocksController.put("/stocks/update/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def updateStock(id:int, data:StockDTO):
    return service.updateStocks(id,data)

@stocksController.delete("/stocks/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteStock(id: int):
    return service.deleteStocks(id)