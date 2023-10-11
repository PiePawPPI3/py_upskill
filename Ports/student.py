class Student:
    def __init__(self, username: str, scores: list[float]):
        self._username = username
        self._scores = scores

    def calculate_average(self) -> float:
        if self._scores:
            return round(sum(self._scores) / len(self._scores), 1)
        else:
            return 0.0

    def has_student_passed(self) -> str:
        if self.calculate_average() >= 2.0 and len(self._scores) >= 3:
            return 'has passed !'
        else:
            return 'has failed !!'

    def display_student_info(self):
        print('Username#: ' + self._username)
        print('Scores#: ' + str(self._scores))
        print('Average#: ' + str(self.calculate_average()))
        print('Passed#: ' + str(self.has_student_passed()))
