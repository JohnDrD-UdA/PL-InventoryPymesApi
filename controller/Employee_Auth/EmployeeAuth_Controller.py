from fastapi import APIRouter
from models.Employee_Auth.EmployeeAuth_DTO import EmployeeAuthDTO
from service.Employee_Auth.EmployeeAuth_Service import AuthService


authController= APIRouter()
service= AuthService()

@authController.post("/auth/create")
def createAuth(data: EmployeeAuthDTO):
    return service.createAuth(data)

@authController.delete("/auth/{id}")
def deleteAuth(id: int):
    return service.deleteAuth(id)

@authController.post("/auth")
def login(data: EmployeeAuthDTO):
    validate= service.validate_credentials(data)
    if validate:
       return service.create_access_token(data)
    else: 
        return "fail"
