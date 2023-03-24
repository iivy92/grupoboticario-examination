from pydantic import BaseModel

class User(BaseModel):
    name: str
    cpf: str
    email: str
    password: str



