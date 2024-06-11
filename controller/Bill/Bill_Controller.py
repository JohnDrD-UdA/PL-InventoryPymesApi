from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from models.Bill.Bill_DTO import BillDTO
from service.Bill.Bill_Service import BillService
from models.Bill.Bill_Buy_DTO import BillBuyDTO


billsController= APIRouter()
service= BillService()
TAG="Bills"
@billsController.get("/bills",dependencies=[Depends(validateToken)],tags=[TAG])
def getBills():
    return service.getBills()

@billsController.get("/bills/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def getBillById(id:int):
    return service.getBillById(id)

@billsController.post("/bills/create",dependencies=[Depends(validateToken)],tags=[TAG])
def createBill(data: BillBuyDTO):
    return service.createBills(data)

@billsController.put("/bills/update/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def updateBill(id:int, data:BillDTO):
    return service.updateBills(id,data)

@billsController.delete("/bills/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteBill(id: int):
    return service.deleteBill(id)