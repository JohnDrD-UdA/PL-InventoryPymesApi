from config.config import session
from models.Product.Product_Table import Products
from models.Product.Product_DTO import ProductDTO

class ProductService():    
    def getProducts(self):
        try:
            result= session.query(Products).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createProducts(self,data: ProductDTO):
        try:
            new_product= Products(name=data.name, unit_cost=data.unit_cost, unit_id=data.unit_id, prov_id=data.prov_id)
            session.add(new_product)
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