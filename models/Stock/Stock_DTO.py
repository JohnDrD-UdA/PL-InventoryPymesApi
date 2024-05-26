from pydantic import BaseModel
from typing import Optional

class StockDTO(BaseModel):

    ammount:Optional[float] 
    product_id:Optional[int] 
    location_id:Optional[int] 