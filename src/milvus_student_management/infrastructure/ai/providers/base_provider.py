from abc import ABC
from abc import abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt: str,
    ) -> str:
        pass