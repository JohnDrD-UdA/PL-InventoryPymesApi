from pydantic import BaseModel
from typing import Optional

class clientDTO(BaseModel):
    id: Optional[str]
    name :str
    lastname :str
    phone : str
    age : int
    gender : Optional[bool]