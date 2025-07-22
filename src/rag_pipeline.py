from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Dict, List, Optional
from interface import (
    BaseDatastore,
    BaseIndexer,
    BaseRetriever,
    BaseResponseGenerator,
    BaseEvaluator,
    EvaluationResult,
)


@dataclass
class RAGPipeline:
    """Main RAG pipeline that orchestrates all components."""

    datastore: BaseDatastore
    indexer: BaseIndexer
    retriever: BaseRetriever
    response_generator: BaseResponseGenerator
    evaluator: Optional[BaseEvaluator] = None

    def reset(self) -> None:
        """Reset the datastore."""
        self.datastore.reset()

    def add_documents(self, documents: List[str]) -> None:
        """Index a list of documents."""
        items = self.indexer.index(documents)
        self.datastore.add_items(items)
        print(f"✅ Added {len(items)} items to the datastore.")

    def process_query(self, query: str) -> str:
        search_results = self.retriever.search(query)
        print(f"✅ Found {len(search_results)} results for query: {query}\n")

        for i, result in enumerate(search_results):
            print(f"🔍 Result {i+1}: {result}\n")

        response = self.response_generator.generate_response(query, search_results)
        return response

    def evaluate(
        self, sample_questions: List[Dict[str, str]]
    ) -> List[EvaluationResult]:
        # Evaluate a list of question/answer pairs.
        questions = [item["question"] for item in sample_questions]
        expected_answers = [item["answer"] for item in sample_questions]

        with ThreadPoolExecutor(max_workers=10) as executor:
            results: List[EvaluationResult] = list(
                executor.map(
                    self._evaluate_single_question,
                    questions,
                    expected_answers,
                )
            )

        for i, result in enumerate(results):
            result_emoji = "✅" if result.is_correct else "❌"
            print(f"{result_emoji} Q {i+1}: {result.question}: \n")
            print(f"Response: {result.response}\n")
            print(f"Expected Answer: {result.expected_answer}\n")
            print(f"Reasoning: {result.reasoning}\n")
            print("--------------------------------")

        number_correct = sum(result.is_correct for result in results)
        print(f"✨ Total Score: {number_correct}/{len(results)}")
        return results

    def _evaluate_single_question(
        self, question: str, expected_answer: str
    ) -> EvaluationResult:
        # Evaluate a single question/answer pair.
        response = self.process_query(question)
        return self.evaluator.evaluate(question, response, expected_answer)
