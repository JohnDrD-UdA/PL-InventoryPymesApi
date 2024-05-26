from pydantic import BaseModel
from typing import Optional

class locationDTO(BaseModel):
    name :str
    manager_id : Optional[int] 
    phone : str
    address : str