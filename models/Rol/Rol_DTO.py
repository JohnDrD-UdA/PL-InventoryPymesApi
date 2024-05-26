from pydantic import BaseModel
from typing import Optional

class RolDTO(BaseModel):

    name:Optional[str] 
    state:Optional[bool] 