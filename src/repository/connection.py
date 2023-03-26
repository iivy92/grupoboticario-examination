from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://default:root@127.0.0.1:5432/cashback"

Base = declarative_base()

class DatabaseConnection:
    def __new__(self) -> Session:
        self._engine = create_engine(SQLALCHEMY_DATABASE_URL)
        Base.metadata.create_all(self._engine)
        return sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
