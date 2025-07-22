from abc import ABC, abstractmethod
from typing import List


class BaseRetriever(ABC):

    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> List[str]:
        pass
