from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    cpf: str
    email: str
    password: str

    @validator('cpf')
    def validate_cpf(cls, cpf):
        pass




