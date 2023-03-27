from src.utils.authenticator import Authenticator
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from validate_docbr import CPF
from dataclasses import dataclass

class User(BaseModel):
    name: str
    cpf: str
    email: EmailStr
    password: str

    @validator('cpf')
    def validate_cpf(cls, cpf: str):
        cpf_validator = CPF()
        if not cpf_validator.validate(cpf):
            raise ValueError("inavlid CPF")
        
        return cpf

    @validator('password')
    def hash_password(cls, password: str):
        authenticator = Authenticator()
        return authenticator.get_hashed_password(password)


class UserCreated(BaseModel):
    id: int
    name: Optional[str]
    cpf: Optional[str]
    email: Optional[EmailStr]

    class Config:
        orm_mode = True


class UserToken(BaseModel):
    access_token: str
    user: Optional[str]
    exp: Optional[str]
