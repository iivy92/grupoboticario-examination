import abc

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self._session = session

    def add(self, model):
        self._session.add(model)
        self._session.commit()

    def get(self, reference):
        return self._session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        return self._session.query(model.Batch).all()


