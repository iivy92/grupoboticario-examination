from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String

from src.repository.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cpf = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String, unique=True)
    date = Column(Date)
    price = Column(Float)
    status = Column(String)
    user_cpf = Column(String, ForeignKey("users.cpf"), index=True)
