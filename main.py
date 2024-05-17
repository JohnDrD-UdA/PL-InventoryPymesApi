from fastapi import FastAPI
from controller.controller import clientController	
app= FastAPI()

app.include_router(clientController)