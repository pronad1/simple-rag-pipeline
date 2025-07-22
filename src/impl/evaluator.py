from interface.base_evaluator import BaseEvaluator, EvaluationResult
from util.invoke_ai import invoke_ai
from util.extract_xml import extract_xml_tag

SYSTEM_PROMPT = """
You are a system that evaluates the correctness of a response to a question.
The question will be provided in <question>...</question> tags.
The response will be provided in <response>...</response> tags.
The expected answer will be provided in <expected_answer>...</expected_answer> tags.

The response doesn't have to exactly match all the words/context the expected answer. It just needs to be right about
the answer to the actual question itself.

Evaluate whether the response is correct or not, and return your reasoning in <reasoning>...</reasoning> tags.
Then return the result in <result>...</result> tags — either as 'true' or 'false'.
"""


class Evaluator(BaseEvaluator):
    def evaluate(
        self, query: str, response: str, expected_answer: str
    ) -> EvaluationResult:

        user_prompt = f"""
        <question>\n{query}\n</question>
        <response>\n{response}\n</response>
        <expected_answer>\n{expected_answer}\n</expected_answer>
        """

        response_content = invoke_ai(
            system_message=SYSTEM_PROMPT, user_message=user_prompt
        )

        reasoning = extract_xml_tag(response_content, "reasoning")
        result = extract_xml_tag(response_content, "result")
        print(response_content)

        if result is not None:
            is_correct = result.lower() == "true"
        else:
            is_correct = False
            reasoning = f"No result found: ({response_content})"

        return EvaluationResult(
            question=query,
            response=response,
            expected_answer=expected_answer,
            is_correct=is_correct,
            reasoning=reasoning,
        )
