import datetime
from ports.student import Student


class EmptyFileError(Exception):
    pass


def read_scores(file_path: str) -> list[Student]:
    with open(file_path, 'r') as file:
        data = file.readlines()

    if not data:
        raise EmptyFileError()

    results = []

    for line in data:
        fields = line.strip().split(',')
        username = fields[0]
        scores = []

        for score in fields:
            try:
                score_value = float(score.strip().replace(',', '', 1))
                scores.append(score_value)
            except ValueError:
                pass

        student = Student(username, scores)
        results.append(student)

    return results


def display_scores(results: list[Student]) -> None:
    print("*** Created at :", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    for student in results:
        student.display_student_info()
        print('_ _ _')
