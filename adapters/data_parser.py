import datetime
from pathlib import Path

from ports.student import Student


class EmptyFileError(Exception):
    pass


class UnsupportedFileFormatError(Exception):
    pass


class AccessDeniedError(Exception):
    pass


# TO DO
class InvalidGradeError(Exception):
    pass


# TO DO
class DataProcessingError(Exception):
    pass


def read_scores(file_path: str) -> list[Student]:
    if not Path(file_path).is_file():
        raise FileNotFoundError()
    if not file_path.lower().endswith('.txt'):
        raise UnsupportedFileFormatError()

    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
    except PermissionError:
        raise AccessDeniedError()

    if not data:
        raise EmptyFileError()

    results = []

    for line in data:
        fields = line.strip().split(',')
        username = fields[0]
        scores = []

        for score in fields[1:]:
            try:
                score_value = float(score.strip().replace(',', '', 1))
                if score_value < 1 or score_value > 6:
                    print(f'Grades beyond the range 1-6=> {score_value}')
                scores.append(score_value)
            except ValueError as e:
                print(f'Error while processing score for {fields[0]}: {e}')
                # raise DataProcessingError(f'Error while processing score for {fields[0]}: {e}') TO DO
                continue

        student = Student(username, scores)
        results.append(student)

    return results


def display_scores(results: list[Student]) -> None:
    print("*** Created at :", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    for student in results:
        student.display_student_info()
        print('_ _ _')
