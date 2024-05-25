from fastapi import FastAPI
from controller.Location.Location_Controller import locationController
from controller.User.User_Controller import userController
app= FastAPI()
app.include_router(locationController)
app.include_router(userController)
