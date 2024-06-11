from fastapi import APIRouter, Depends
from controller.MW.MW import validateToken
from models.Rol.Rol_DTO import RolDTO
from service.Rol.Rol_Service import RolService


rolesController= APIRouter()
service= RolService()
TAG="Roles"
@rolesController.get("/roles",dependencies=[Depends(validateToken)],tags=[TAG])
def getRol():
    return service.getRoles()

@rolesController.get("/roles/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def getRolById(id:int):
    return service.getRolById(id)

@rolesController.post("/roles/create",dependencies=[Depends(validateToken)],tags=[TAG])
def createRol(data: RolDTO):
    return service.createRoles(data)

@rolesController.put("/roles/update/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def updateRol(id:int, data:RolDTO):
    return service.updateRoles(id,data)

@rolesController.delete("/roles/{id}",dependencies=[Depends(validateToken)],tags=[TAG])
def deleteRol(id: int):
    return service.deleteRoles(id)