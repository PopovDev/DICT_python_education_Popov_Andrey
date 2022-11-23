"""Module for different math tests."""
from abc import ABC, abstractmethod
import random
from typing import Literal
from question_generator import MathQuestionGenerator
from math_log import MathLogger
from math_question import MathQuestion


class MathTest(ABC):
    """Abstract class for math test"""

    def __init__(self):
        """Initialize test"""
        self.questions: list[MathQuestion] = []
        self.score = 0
        self.logger = MathLogger()

    @abstractmethod
    def generate_questions(self):
        """Generate questions for test"""

    @staticmethod
    def __get_answer() -> int | float:
        """Get answer from user"""
        while True:
            answer = input("Answer: >")
            try:
                return int(answer)
            except ValueError:
                try:
                    return float(answer)
                except ValueError:
                    print("Wrong answer. Try again.")

    def __string_prompt(self, prompt: str) -> str:
        """Get string from user"""
        while True:
            answer = input(prompt)
            if answer:
                return answer
            print("Wrong answer. Try again.")

    def __save_prompt(self):
        """Request user to save log"""
        print("Would you like to save the result? Enter yes or no.")
        answer = input("> ")
        if answer == "yes":
            name = self.__string_prompt("Enter your name: >")
            self.logger.save(name)

    @property
    @abstractmethod
    def name(self) -> str:
        """Get name of test"""

    def start_session(self):
        """Start session of current test with parameters"""
        self.logger.log_start_session(self.name)

    def start(self):
        """Start test"""
        self.generate_questions()
        self.start_session()
        for question in self.questions:
            print(f"Question: {question} ?")
            answer = self.__get_answer()
            if question.check_answer(answer):
                print("Correct!")
                self.score += 1
            else:
                print("Wrong!")
            self.logger.log_answer(question, answer)
        print(f"Your mark is {self.score}/{len(self.questions)}.")
        self.logger.log_score(self.score)
        self.logger.log_end_session()
        self.__save_prompt()


class EasyMathTest(MathTest):
    """Class of easy math test"""

    def generate_questions(self):
        """Generate questions for test"""
        for _ in range(5):
            question = MathQuestionGenerator.generate_easy_question()
            self.questions.append(question)

    @property
    def name(self) -> str:
        """Get name of test"""
        return "Easy"


class MediumMathTest(MathTest):
    """Class of medium math test"""

    def generate_questions(self):
        """Generate questions for test"""
        for _ in range(7):
            question = MathQuestionGenerator.generate_medium_question()
            self.questions.append(question)

    @property
    def name(self) -> str:
        """Get name of test"""
        return "Medium"


class HardMathTest(MathTest):
    """Class of hard math test"""

    def generate_questions(self):
        """Generate questions for test"""
        for _ in range(9):
            self.questions.append(
                MathQuestionGenerator.generate_hard_question())

    @property
    def name(self) -> str:
        """Get name of test"""
        return "Hard"


class InsaneMathTest(MathTest):
    """Class of insane math test"""

    def generate_questions(self):
        """Generate questions for test"""
        for _ in range(11):
            self.questions.append(
                MathQuestionGenerator.generate_insane_question())

    @property
    def name(self) -> str:
        """Get name of test"""
        return "Insane"


class TournamentMathTest(MathTest):
    """Class of tournament math test"""

    def generate_questions(self):
        """Generate questions for test"""
        for _ in range(5):
            self.questions.append(
                MathQuestionGenerator.generate_easy_question())
            self.questions.append(
                MathQuestionGenerator.generate_medium_question())
            self.questions.append(
                MathQuestionGenerator.generate_hard_question())
            self.questions.append(
                MathQuestionGenerator.generate_insane_question())
        random.shuffle(self.questions)

    @property
    def name(self) -> str:
        """Get name of test"""
        return "Tournament"


class MathTestFactory:
    """Factory class for getting test"""
    @staticmethod
    def get_test(test_name: Literal["easy", "medium", "hard", "insane", "tournament"]) -> MathTest:
        """Get test by name"""
        tests = {
            "easy": EasyMathTest,
            "medium": MediumMathTest,
            "hard": HardMathTest,
            "insane": InsaneMathTest,
            "tournament": TournamentMathTest
        }
        return tests[test_name]()

    @staticmethod
    def create_test(level: int) -> MathTest:
        """Create test by level"""
        difficulty = {
            1: "easy",
            2: "medium",
            3: "hard",
            4: "insane",
            5: "tournament"
        }
        if level not in difficulty:
            raise ValueError("Wrong level")
        return MathTestFactory.get_test(difficulty[level])
