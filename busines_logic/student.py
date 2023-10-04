class Student:
    def __init__(self, username: str, scores: list[float]):
        self.username = username
        self.scores = scores

    def calculate_average(self) -> float:
        if self.scores:
            return round(sum(self.scores) / len(self.scores), 1)
        else:
            return 0

    def display_student_info(self):
        print('Username#: ' + self.username)
        print('Scores#: ' + self.scores)
