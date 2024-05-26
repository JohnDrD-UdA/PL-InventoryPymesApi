from pydantic import BaseModel
from typing import Optional

class UserDTO(BaseModel):
    name :str
    phone : str
    address: str
    mail: str
    rol_id: Optional[int]