from pydantic import BaseModel
from typing import Optional

class ProductDTO(BaseModel):

    name:Optional[str] 
    unit_cost:Optional[float] 
    unit_id:Optional[int] 
    prov_id:Optional[int] 