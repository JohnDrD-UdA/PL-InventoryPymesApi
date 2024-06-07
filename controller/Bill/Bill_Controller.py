from fastapi import APIRouter
from models.Bill.Bill_DTO import BillDTO
from service.Bill.Bill_Service import BillService
from models.Bill.Bill_Buy_DTO import BillBuyDTO


billsController= APIRouter()
service= BillService()

@billsController.get("/bills")
def getBills():
    return service.getBills()

@billsController.get("/bills/{id}")
def getBillById(id:int):
    return service.getBillById(id)

@billsController.post("/bills/create")
def createBill(data: BillBuyDTO):
    return service.createBills(data)

@billsController.put("/bills/update/{id}")
def updateBill(id:int, data:BillDTO):
    return service.updateBills(id,data)

@billsController.delete("/bills/{id}")
def deleteBill(id: int):
    return service.deleteBill(id)