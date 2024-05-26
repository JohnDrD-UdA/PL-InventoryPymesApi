from config.config import session
from models.Stock.Stock_Table import Stocks
from models.Stock.Stock_DTO import StockDTO

class StockService():    
    def getStocks(self):
        try:
            result= session.query(Stocks).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createStocks(self,data: StockDTO):
        try:
            new_stock= Stocks(ammount=data.ammount, product_id=data.product_id, location_id=data.location_id)
            session.add(new_stock)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
    def updateStocks(self,id:int,data:StockDTO):
        try:
            stock= session.query(Stocks).get(id)
            if stock:
                stock.ammount= data.ammount
                stock.unit_cost=data.product_id
                stock.unit_id=data.location_id
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def deleteStocks(self,id:int):
        try:
            stock= session.query(Stocks).get(id)
            if stock:
                session.delete(stock)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def getStockById(seld,id:int):
        try:
            result= session.query(Stocks).get(id)
            if result:
                return result
            return "404"
        except Exception as e:
            print(e)
            return "fail"