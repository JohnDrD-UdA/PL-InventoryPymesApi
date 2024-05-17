from pydantic import BaseModel
from typing import Optional

class UserDTO(BaseModel):
    id: Optional[str]
    name :str
    phone : str
    address: str
    mail: str
    rol_id: Optional[int]