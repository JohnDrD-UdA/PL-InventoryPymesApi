from config.config import session
from models.Employee_Auth.EmployeeAuth import EmployeeAuth
from models.Employee_Auth.EmployeeAuth_DTO import EmployeeAuthDTO
from passlib.context import CryptContext
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from typing import Union, Any
from jose import jwt

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class AuthService():
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
    ALGORITHM = "HS256"
    JWT_SECRET_KEY = "VmDxQwkN12OqsMfknoAc"
    JWT_REFRESH_SECRET_KEY = "HCUwErZMfhKW5GXT0Xwl"
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    def createAuth(self,data: EmployeeAuthDTO):
        try:
            password_hash= self.get_hashed_password(data.password)
            date= int(datetime.now().timestamp()*1000)
            new_user= EmployeeAuth(user_name=data.userName, last_login=date, state=data.state, user_id=data.user_id,password=password_hash)
            session.add(new_user)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
        
    def deleteAuth(self,id:int):
        try:
            user= session.query(EmployeeAuth).get(id)
            if user:
                session.delete(user)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
        
    def create_access_token(self,data: EmployeeAuthDTO, expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.now(timezone.utc) + expires_delta
        else:
            expires_delta= datetime.now(timezone.utc) + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = {"exp": expires_delta, "sub": str(data.userName)}
        print(f"exp: {expires_delta}")
        encoded_jwt = jwt.encode(to_encode, self.JWT_SECRET_KEY, self.ALGORITHM)
        return encoded_jwt
    
    def create_refresh_token(self,subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.now(timezone.utc) + expires_delta
        else:
            expires_delta = datetime.now(timezone.utc) + timedelta(minutes=self.REFRESH_TOKEN_EXPIRE_MINUTES)
    
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, self.JWT_REFRESH_SECRET_KEY, self.ALGORITHM)
        return encoded_jwt
    
    def get_hashed_password(self,password: str) -> str:
        return self.password_context.hash(password)

    def verify_password(self,password: str, hashed_pass: str) -> bool:
        return self.password_context.verify(password, hashed_pass)
    def validate_credentials(self,data:EmployeeAuthDTO):
        user= session.query(EmployeeAuth).filter(EmployeeAuth.user_name == data.userName).first()
        if user:
             result=self.verify_password(data.password, user.password)
             return result
        return False