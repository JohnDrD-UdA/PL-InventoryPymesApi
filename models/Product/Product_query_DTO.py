from pydantic import BaseModel
from typing import Optional

class ProductQueryDTO(BaseModel):

    name:Optional[str] 
    unit_cost:Optional[float] 
    unit:Optional[str]
    location:Optional[int]
    amount: Optional[float]
    prov_id:Optional[int] 