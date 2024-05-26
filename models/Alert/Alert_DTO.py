from pydantic import BaseModel
from typing import Optional

class AlertDTO(BaseModel):

    msg:Optional[str] 
    date_created:Optional[int]
    type_id:Optional[int] 
    state:Optional[bool] 