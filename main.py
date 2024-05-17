from fastapi import FastAPI
from controller.Location.Location_Controller import locationController
app= FastAPI()

app.include_router(locationController)