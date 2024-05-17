from sqlalchemy import or_
from config.config import conn
from models.clients import Client
from models.client_model import clientDTO

class ClientService():    
    def getClients(self):
        result=conn.execute(Client.select())
        resultAsList=[r._asdict() for r in result]
        return resultAsList
    
    def createClient(self,data: clientDTO):
        return conn.execute(Client.insert().values(data.__dict__))
    
    def updateClient(self,id:int,data:clientDTO):
        values= data.__dict__
        print(values)
        conn.execute(Client.update().where(Client.c.id == id).values(values))
        return values
    def deleteClient(self,id:int):
        return conn.execute(Client.delete().where(Client.c.id == id))