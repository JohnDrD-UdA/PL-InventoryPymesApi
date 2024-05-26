from fastapi import APIRouter
from models.Product.Product_DTO import ProductDTO
from service.Product.Product_Service import ProductService


productsController= APIRouter()
service= ProductService()

@productsController.get("/products")
def getProduct():
    return service.getProducts()

@productsController.get("/products/{id}")
def getProductById(id:int):
    return service.getProductById(id)

@productsController.post("/products/create")
def createProduct(data: ProductDTO):
    return service.createProducts(data)

@productsController.put("/products/update/{id}")
def updateProduct(id:int, data:ProductDTO):
    return service.updateProducts(id,data)

@productsController.delete("/products/{id}")
def deleteProduct(id: int):
    return service.deleteProducts(id)