from pydantic import BaseModel
from models.Stock.Stock_DTO import StockDTO
class BillBuyDTO(BaseModel):
    client_id:int 
    owner_id:int
    product_ids: list[StockDTO]
    state:str