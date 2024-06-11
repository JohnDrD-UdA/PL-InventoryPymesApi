from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from models.Employee_Auth.EmployeeAuth_DTO import EmployeeAuthDTO
from service.Employee_Auth.EmployeeAuth_Service import AuthService


authController= APIRouter()
service= AuthService()
TAG="Auth"
@authController.post("/auth/create",dependencies=[Depends(validateToken)],tags=[TAG])
def createAuth(data: EmployeeAuthDTO):
    return service.createAuth(data)

@authController.delete("/auth/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteAuth(id: int):
    return service.deleteAuth(id)

@authController.post("/auth",tags=[TAG])
def login(data: EmployeeAuthDTO):
    validate= service.validate_credentials(data)
    if validate:
       return service.create_access_token(data)
    else: 
        return "fail"
