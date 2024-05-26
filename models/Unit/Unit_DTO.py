from pydantic import BaseModel
from typing import Optional

class UnitDTO(BaseModel):

    name:Optional[str] 
    state:Optional[bool] 