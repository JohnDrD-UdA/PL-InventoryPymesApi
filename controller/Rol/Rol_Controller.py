from fastapi import APIRouter
from models.Rol.Rol_DTO import RolDTO
from service.Rol.Rol_Service import RolService


rolesController= APIRouter()
service= RolService()

@rolesController.get("/roles")
def getRol():
    return service.getRoles()

@rolesController.get("/roles/{id}")
def getRolById(id:int):
    return service.getRolById(id)

@rolesController.post("/roles/create")
def createRol(data: RolDTO):
    return service.createRoles(data)

@rolesController.put("/roles/update/{id}")
def updateRol(id:int, data:RolDTO):
    return service.updateRoles(id,data)

@rolesController.delete("/roles/{id}")
def deleteRol(id: int):
    return service.deleteRoles(id)