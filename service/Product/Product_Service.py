from config.config import session
from models.Product.Product_Table import Products
from models.Product.Product_DTO import ProductDTO
from models.Stock.Stock_Table import Stocks
from models.Product.Product_query_DTO import ProductQueryDTO
from models.Unit.Unit_Table import Units

class ProductService():    
    def getProducts(self):
        try:
            products= session.query(Products, Stocks, Units
            ).filter(Stocks.product_id==Products.id
            ).all()
            print(products[0]._asdict())

            
            #result=[products[i]._data for i in range(len(products))]
            result=[self.formatProduct(products[i]._asdict()) for i in range(len(products))]
            return result

        except Exception as e:
            print(e)
            return "fail"
        
    def formatProduct(self,data: dict):
        format= ProductQueryDTO(name=data["Products"].name, 
    unit_cost=data["Products"].unit_cost, 
    unit=data["Units"].name,
    location=data["Stocks"].location_id,
    amount= data["Stocks"].amount,
    prov_id= data["Products"].prov_id)
        return format
    def createProducts(self,data: ProductDTO):
        try:
            new_product= Products(name=data.name, unit_cost=data.unit_cost, unit_id=data.unit_id, prov_id=data.prov_id)
            session.add(new_product)
            session.commit()
            new_stock= Stocks(amount=0, location_id= data.location, product_id=new_product.id)
            session.add(new_stock)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
    def updateProducts(self,id:int,data:ProductDTO):
        try:
            product= session.query(Products).get(id)
            if product:
                product.name= data.name
                product.unit_cost=data.unit_cost
                product.unit_id=data.unit_id
                product.prov_id=data.prov_id
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def deleteProducts(self,id:int):
        try:
            product= session.query(Products).get(id)
            if product:
                session.delete(product)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def getProductById(seld,id:int):
        try:
            result= session.query(Products).get(id)
            if result:
                return result
            return "404"
        except Exception as e:
            print(e)
            return "fail"