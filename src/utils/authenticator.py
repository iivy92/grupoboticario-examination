from passlib.context import CryptContext
import jwt
import datetime
from fastapi.security import OAuth2PasswordBearer

SECRET = 'my-secret'


class Authenticator:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get_reuseable_oauth(self):
        reuseable_oauth = OAuth2PasswordBearer(tokenUrl="/signin", scheme_name="JWT")
        return reuseable_oauth

    def verify_hashed_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_hashed_password(self, password: str):
        return self.pwd_context.hash(password)

    def generate_jwt_token(self, user):
        jwt_payload = {
            "user": user.cpf,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        return jwt.encode(jwt_payload, SECRET, algorithm="HS256")