
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from datetime import datetime, timezone
ALGORITHM = "HS256"
JWT_SECRET_KEY = "VmDxQwkN12OqsMfknoAc"
security = HTTPBearer()
def validateToken(credentials: HTTPAuthorizationCredentials = Security(security)):
    token: str = credentials.credentials
    payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM] )
    
    if datetime.fromtimestamp(payload['exp']) <= datetime.now():
        return True
    return False