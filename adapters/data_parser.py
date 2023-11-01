import datetime

from ports.custom_errors import CustomErrors
from ports.student import Student


def read_scores(file_path: str) -> list[Student]:
    try:
        if not file_path.lower().endswith('.txt'):
            raise CustomErrors.UnsupportedFileFormatError()
        with open(file_path, 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        raise CustomErrors.FileNotFound()
    except PermissionError:
        raise CustomErrors.AccessDeniedError()
    except UnicodeDecodeError:
        raise CustomErrors.BinaryFileError()
    except OSError:
        raise CustomErrors.AccessDeniedError()

    if not data:
        raise CustomErrors.EmptyFileError()

    results = []

    for line in data:
        fields = line.strip().split(',')
        username = fields[0]
        scores = []

        for score in fields[1:]:
            try:
                score_value = float(score.strip().replace(',', '', 1))
                if score_value < 1 or score_value > 6:
                    raise CustomErrors.InvalidGradeError()
                scores.append(score_value)
            except ValueError:
                raise CustomErrors.DataProcessingError()

        student = Student(username, scores)
        results.append(student)

    return results


def display_scores(results: list[Student]) -> None:
    print("*** Created at :", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    for student in results:
        student.display_student_info()
        print('_ _ _')
