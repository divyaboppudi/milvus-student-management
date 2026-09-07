from abc import ABC, abstractmethod
from typing import Any


class IEntityRepository(ABC):

    @abstractmethod
    def create(self, entity: Any) -> str:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: str) -> Any:
        pass

    @abstractmethod
    def update(self, entity: Any) -> bool:
        pass

    @abstractmethod
    def delete(self, entity_id: str) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> list[Any]:
   