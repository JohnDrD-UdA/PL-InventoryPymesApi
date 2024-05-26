from pydantic import BaseModel
from typing import Optional

class BillDTO(BaseModel):
    final_cost: float
    date_created:int
    date_paid:Optional[int] 
    state:str
    client_id:Optional[int] 
    owner_id:Optional[int] 