from pydantic import BaseModel
from typing import Optional

class AlertTypeDTO(BaseModel):

    name:Optional[str] 
    state:Optional[bool] 