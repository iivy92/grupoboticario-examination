from src.utils.hasher import Hasher
from pydantic import BaseModel, validator
from validate_docbr import CPF

class User(BaseModel):
    name: str
    cpf: str
    email: str
    password: str

    @validator('cpf')
    def validate_cpf(cls, cpf: str):
        cpf_validator = CPF()
        if not cpf_validator.validate(cpf):
            raise ValueError("inavlid CPF")
        
        return cpf

    @validator('password')
    def hash_password(cls, password: str):
        hasher = Hasher()
        return hasher.get_hashed_password(password)




