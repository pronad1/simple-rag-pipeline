from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel


class DataItem(BaseModel):
    content: str = ""
    source: str = ""


class BaseDatastore(ABC):
    @abstractmethod
    def add_items(self, items: List[DataItem]) -> None:
        pass

    @abstractmethod
    def get_vector(self, content: str) -> List[float]:
        pass

    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> List[str]:
        pass
