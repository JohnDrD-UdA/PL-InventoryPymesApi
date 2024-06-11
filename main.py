from config.config import Base,engine
from fastapi import FastAPI
from controller.Location.Location_Controller import locationController
from controller.User.User_Controller import userController
from controller.Alert.Alert_Controller import alertController
from controller.Alert_Type.Alert_Type_Controller import alertTypeController
from controller.Bill.Bill_Controller import billsController
from controller.Employee_Auth.EmployeeAuth_Controller import authController
from controller.Product.Product_Controller import productsController
from controller.Rol.Rol_Controller import rolesController
from controller.Stock.Stock_Controller import stocksController
from controller.Unit.Unit_Controller import unitsController

Base.metadata.create_all(engine)

app= FastAPI()
app.include_router(authController)
app.include_router(productsController)
app.include_router(billsController)
app.include_router(userController)
app.include_router(locationController)
app.include_router(alertController)
app.include_router(alertTypeController)
app.include_router(rolesController)
app.include_router(stocksController)

