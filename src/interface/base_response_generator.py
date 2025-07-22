from abc import ABC, abstractmethod
from typing import List


class BaseResponseGenerator(ABC):

    @abstractmethod
    def generate_response(self, query: str, context: List[str]) -> str:
        pass
