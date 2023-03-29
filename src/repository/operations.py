import abc
from datetime import date, timedelta
from sqlalchemy.orm import Session

from src.repository import models
from src.schemas.user import User


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, model):
        raise NotImplementedError

    # @abc.abstractmethod
    # def get(self, reference):
    #     raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_cpf(self, user: User):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self._session = session()

    def add(self, model):
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return model

    def get_user_by_cpf(self, cpf: str):
        return self._session.query(models.User).filter_by(cpf=cpf).one_or_none()
    
    def get_items_by_cpf(self, cpf: str, date: date):
        inicial_date = date - timedelta(days=30)
        return self._session.query(models.Item).filter_by(user_cpf=cpf).filter(models.Item.date.between(inicial_date, date))

    # def get(self, reference):
    #     return self._session.query(model.Batch).filter_by(reference=reference).one()

    # def list(self):
    #     return self._session.query(model.Batch).all()
