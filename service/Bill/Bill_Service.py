from sqlalchemy import and_
from config.config import session
from models.Bill.Bill_table import Bills
from models.Bill.Bill_DTO import BillDTO
from models.Bill.Bill_Buy_DTO import BillBuyDTO
from models.Product.Product_Table import Products
from models.Stock.Stock_DTO import StockDTO
from models.Bill_Item.Billitem import Bill_Items
from datetime import datetime
from models.Stock.Stock_Table import Stocks

class BillService():    
    def getBills(self):
        try:
            result= session.query(Bills).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createBills(self,data: BillBuyDTO):
        try:    
            self.updateStock(data.product_ids)
            billProductInfo=self.generateProductBill(data.product_ids)
            date= int(datetime.now().timestamp()*1000)
            new_bill= Bills(final_cost=billProductInfo["total"], date_created=date, state=data.state, client_id=data.client_id,owner_id= data.owner_id)
            session.add(new_bill)
            session.commit()
            for item in billProductInfo["items"]:
                item.bill_id= new_bill.id
            session.add_all(billProductInfo["items"])
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "Unvalid Stock"
    def generateProductBill(self, ids:list[StockDTO]):
            
            billItems=list()
            product_ids= list(map(lambda x: x.product_id, ids))
            products= session.query(Products).filter(Products.id.in_(product_ids)).all()
            total_cost= 0

            for product in products:

                cost= product.unit_cost* list(filter(lambda x: x.product_id== product.id, ids))[0].ammount
                total_cost+=cost

                new_BillItem= Bill_Items(product_id= product.id,ammount= cost, bill_id=0)
                print(f"item: {cost}")
                billItems.append(new_BillItem)

            return {"total": total_cost, "items": billItems}
    def updateStock(self,items:list[StockDTO]):
        commit=True
        for item in items:
            stock= session.query(Stocks).filter(and_(Stocks.location_id== item.location_id,Stocks.product_id==item.product_id)).first()
            print(f"{stock.id}, {item.ammount}")
            if stock:
                if stock.amount >=item.ammount:
                    stock.amount-=item.ammount
                    continue
                commit=False
            else:
                commit=False
                break
        if commit:
            return session.commit()
        else:
            raise Exception("Unvalid Stock")
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