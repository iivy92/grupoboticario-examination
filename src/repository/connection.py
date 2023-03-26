from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

Base = declarative_base()

class DatabaseConnection:
    def __init__(self) -> None:
        self._engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
    
    def __new__(self) -> Session:
        session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        try:
            yield session
        finally:
            session.close()
