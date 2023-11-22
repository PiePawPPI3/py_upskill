
from ports.data_parser import UnsupportedFileFormatError, FileNotFound, AccessDeniedError, BinaryFileError, \
    EmptyFileError, InvalidGradeError, DataProcessingError, UnknownError, FileSaveError
from ports.student import Student


def read_scores(file_path: str) -> list[Student]:
    try:
        if not file_path.lower().endswith('.txt'):
            raise UnsupportedFileFormatError()
        with open(file_path, 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        raise FileNotFound
    except PermissionError:
        raise AccessDeniedError
    except UnicodeDecodeError:
        raise BinaryFileError
    except OSError:
        raise UnknownError

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
                    raise InvalidGradeError
                scores.append(score_value)
            except ValueError:
                raise DataProcessingError

        student = Student(username, scores)
        results.append(student)

    return results
