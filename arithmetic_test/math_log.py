"""Module for Math log classes"""
from dataclasses import dataclass
from datetime import datetime
from typing import Literal
from math_question import MathQuestion


@dataclass
class MathLog:
    """Class of math log"""
    log_type: Literal["answer", "start", "end", "score"]
    value: str

    def __str__(self) -> str:
        """Return string representation of log"""
        return f"{self.log_type} > {self.value}"


class MathLogger:
    """Class of math logger"""

    def __init__(self):
        """Initialize logger"""
        self.log: list[MathLog] = []

    def __log(self, log: MathLog):
        """Post log to log list"""
        self.log.append(log)

    def save(self, name: str):
        """Save result to file"""
        with open("result.txt", "a", encoding="utf-8") as file:
            file.write(f"Session: {name}\n")
            for log in self.log:
                file.write(f"{log}\n")
            file.write("\n")

    def log_start_session(self, level: str = "None"):
        """Start Log session"""
        record = f"{self.__get_time()} {level}"
        self.__log(MathLog("start", record))

    def log_answer(self, question: MathQuestion, answer: int | float):
        """Log answer"""
        record = f"{question} = {answer} ({question.check_answer(answer)}) -> {question.answer}"
        self.__log(MathLog("answer", record))

    def log_end_session(self):
        """End log session"""
        self.__log(MathLog("end", self.__get_time()))

    def log_score(self, score: int):
        """Log score"""
        self.__log(MathLog("score", f"{score}"))

    @staticmethod
    def __get_time() -> str:
        """Get current time"""
        return datetime.now().strftime("%d.%m.%Y %H:%M:%S")
