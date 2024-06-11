from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from models.User.User_DTO import UserDTO
from service.User.User_Service import UserService


userController= APIRouter()
service= UserService()
TAG="Users"
@userController.get("/users",dependencies=[Depends(validateToken)],tags=[TAG])
def getUsers():
    return service.getUsers()

@userController.get("/user/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def getUserById(id:int):
    return service.getUserById(id)

@userController.post("/users/create",dependencies=[Depends(validateToken)],tags=[TAG])
def createUser(data: UserDTO):
    return service.createUsers(data)

@userController.put("/users/update/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def updateUser(id:int, data:UserDTO):
    return service.updateUsers(id,data)

@userController.delete("/users/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteUser(id: int):
    return service.deleteUser(id)