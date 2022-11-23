"""Module for math question class."""


class MathQuestion:
    """Class that represents a math question."""

    def __init__(self, question: str, answer: int | float):
        """Initialize question"""
        self.question = question
        self.answer = answer

    def check_answer(self, answer: int | float) -> bool:
        """Check answer"""
        return self.answer == answer

    def __str__(self) -> str:
        """Return string representation of question"""
        return self.question
