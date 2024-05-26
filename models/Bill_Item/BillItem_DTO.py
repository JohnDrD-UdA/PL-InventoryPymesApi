from pydantic import BaseModel
from typing import Optional

class BillItemDTO(BaseModel):

    ammount:Optional[float] 
    product_id:Optional[int] 
    bill_id:Optional[int] 