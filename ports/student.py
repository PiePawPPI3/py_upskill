class Student:
    def __init__(self, username: str, scores: list[float]):
        self._username = username
        self._scores = scores
        self._average = None

    def calculate_average(self) -> float:
        if self._scores:
            return round(sum(self._scores) / len(self._scores), 1)
        else:
            return 0.0

    def has_student_passed(self) -> bool:

        if self._average and self._average >= 2.0 and len(self._scores) >= 3:
            return True
        else:
            return False

    def display_student_info(self):
        print('Username#: ' + self._username)
        print('Scores#: ' + str(self._scores))
        print('Average#: ' + str(self.calculate_average()))

        if self.has_student_passed():
            print('Passed#: Passed')
        else:
            print('Passed#: Failed')
