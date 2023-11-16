from typing import Optional


class Student:
    def __init__(self, username: str, scores: list[float]):
        self._username = username
        self._scores = scores
        self._average: Optional[float] = None

    def calculate_average(self) -> float:
        if self._average is None:
            if self._scores:
                average = round(sum(self._scores) / len(self._scores), 1)
            else:
                average = 0.0
            self._average = average
        return self._average

    def has_student_passed(self) -> bool:
        average = self.calculate_average()

        return average >= 2.0 and len(self._scores) >= 3

    def display_student_info(self) -> str:
        student_info = (
            f"Username#: {self._username}\n"
            f"Scores#: {self._scores}\n"
            f"Average#: {self.calculate_average()}\n"
            f"Passed#: {'Passed' if self.has_student_passed() else 'Failed'}"
        )
        return student_info
