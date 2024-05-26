from config.config import session
from models.Bill_Item.Billitem import Bill_Items
from models.Bill_Item.BillItem_DTO import BillItemDTO


class ItemService():    
    def getItem(self):
        try:
            result= session.query(Bill_Items).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createItem(self,data: BillItemDTO):
        try:
            new_Item= Bill_Items(ammount=data.ammount, product_id=data.product_id, bill_id=data.bill_id)
            session.add(new_Item)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
    def updateItem(self,id:int,data:BillItemDTO):
        try:
            Item= session.query(Bill_Items).get(id)
            if Item:
                Item.ammount= data.ammount
                Item.product_id=data.product_id
                Item.bill_id=data.bill_id
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def deleteItem(self,id:int):
        try:
            Item= session.query(Bill_Items).get(id)
            if Item:
                session.delete(Item)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def getItemById(seld,id:int):
        try:
            result= session.query(Bill_Items).get(id)
            if result:
                return result
            return "404"
        except Exception as e:
            print(e)
            return "fail"