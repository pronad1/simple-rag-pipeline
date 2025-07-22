from abc import ABC, abstractmethod
from typing import Optional
from pydantic import BaseModel


class EvaluationResult(BaseModel):
    question: str
    response: str
    expected_answer: str
    is_correct: bool
    reasoning: Optional[str] = None


class BaseEvaluator(ABC):
    """Base interface for the evaluation component."""

    @abstractmethod
    def evaluate(
        self, query: str, response: str, expected_answer: str
    ) -> EvaluationResult:
        pass
