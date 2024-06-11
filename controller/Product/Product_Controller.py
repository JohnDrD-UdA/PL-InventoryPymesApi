from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from models.Product.Product_DTO import ProductDTO
from service.Product.Product_Service import ProductService


productsController= APIRouter()
service= ProductService()
TAG="Products"
@productsController.get("/products",dependencies=[Depends(validateToken)],tags=[TAG])
def getProduct():
    return service.getProducts()

@productsController.get("/products/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def getProductById(id:int):
    return service.getProductById(id)

@productsController.post("/products/create",dependencies=[Depends(validateToken)],tags=[TAG])
def createProduct(data: ProductDTO):
    return service.createProducts(data)

@productsController.put("/products/update/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def updateProduct(id:int, data:ProductDTO):
    return service.updateProducts(id,data)

@productsController.delete("/products/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteProduct(id: int):
    return service.deleteProducts(id)