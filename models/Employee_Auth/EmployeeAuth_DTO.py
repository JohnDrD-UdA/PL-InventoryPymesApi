from pydantic import BaseModel
from typing import Optional

class EmployeeAuthDTO(BaseModel):

    userName:Optional[str] 
    last_login:Optional[int] 
    state: Optional[bool]
    user_id:Optional[int]