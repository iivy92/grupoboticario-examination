import abc
from src.repository import models
from src.domain.user import User
from sqlalchemy.orm import Session


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
    
    def get_user_by_cpf(self, user: User):
        return self._session.query(models.User).filter_by(cpf=user.cpf).one_or_none()

    # def get(self, reference):
    #     return self._session.query(model.Batch).filter_by(reference=reference).one()

    # def list(self):
    #     return self._session.query(model.Batch).all()


