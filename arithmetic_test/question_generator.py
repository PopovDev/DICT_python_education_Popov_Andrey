"""Module for math question generator."""
import random
from math_question import MathQuestion


class MathQuestionGenerator:
    """Class for generating math questions."""

    @classmethod
    def generate_question(cls, difficulty: int) -> MathQuestion:
        """Generate math question with given difficulty."""
        if difficulty == 1:
            return cls.generate_easy_question()
        if difficulty == 2:
            return cls.generate_medium_question()
        if difficulty == 3:
            return cls.generate_hard_question()
        if difficulty == 4:
            return cls.generate_insane_question()
        raise ValueError("Difficulty must be between 1 and 3")

    @classmethod
    def generate_easy_question(cls) -> MathQuestion:
        """Generate easy math question."""
        first_number = random.randint(2, 10)
        second_number = random.randint(2, 10)
        operation = random.choice(("+", "-"))

        if operation == "+":
            answer = first_number + second_number
        else:
            answer = first_number - second_number

        question = f"{first_number} {operation} {second_number}"
        return MathQuestion(question, answer)

    @classmethod
    def generate_medium_question(cls) -> MathQuestion:
        """Generate medium math question."""
        number = random.randint(11, 29)
        answer = number ** 2
        question = f"{number}^2"
        return MathQuestion(question, answer)

    @classmethod
    def generate_hard_question(cls) -> MathQuestion:
        """Generate hard math question."""
        first_number = random.randint(10, 200)
        second_number = random.randint(10, 200)
        answer = first_number * second_number
        question = f"{first_number} * {second_number}"
        return MathQuestion(question, answer)

    @classmethod
    def generate_insane_question(cls) -> MathQuestion:
        """Generate insane math question."""
        first_number = random.randint(10, 200)
        second_number = random.randint(10, 200)
        third_number = random.randint(10, 200)
        answer = first_number * second_number * third_number
        question = f"{first_number} * {second_number} * {third_number}"
        return MathQuestion(question, answer)
