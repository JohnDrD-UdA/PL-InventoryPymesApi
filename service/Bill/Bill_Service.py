from sqlalchemy import or_
from config.config import session
from models.Bill.Bill_table import Bills
from models.Bill.Bill_DTO import BillDTO

class BillService():    
    def getBills(self):
        try:
            result= session.query(Bills).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createBills(self,data: BillDTO):
        try:
            new_bill= Bills(final_cost=data.final_cost, date_created=data.date_created, state=data.state, client_id=data.client_id,owner_id= data.owner_id)
            session.add(new_bill)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
    def updateBills(self,id:int,data:BillDTO):
        try:
            bill= session.query(Bills).get(id)
            if bill:
                bill.final_cost= data.final_cost
                bill.date_created=data.date_created
                bill.state=data.state
                bill.client_id=data.client_id
                bill.owner_id= data.owner_id
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def deleteBill(self,id:int):
        try:
            bill= session.query(Bills).get(id)
            if bill:
                session.delete(bill)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def getBillById(seld,id:int):
        try:
            result= session.query(Bills).get(id)
            if result:
                return result
            return "404"
        except Exception as e:
            print(e)
            return "fail"