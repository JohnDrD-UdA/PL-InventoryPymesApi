from fastapi import APIRouter
from models.User.User_DTO import UserDTO
from service.User.User_Service import UserService


userController= APIRouter()
service= UserService()

@userController.get("/users")
def getUsers():
    return service.getUsers()

@userController.get("/user/{id}")
def getUserById(id:int):
    return service.getUserById(id)

@userController.post("/users/create")
def createUser(data: UserDTO):
    return service.createUsers(data)

@userController.put("/users/update/{id}")
def updateUser(id:int, data:UserDTO):
    return service.updateUsers(id,data)

@userController.delete("/users/{id}")
def deleteUser(id: int):
    return service.deleteUser(id)