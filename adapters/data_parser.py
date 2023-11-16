import datetime
from typing import Optional

from adapters.data_saver import FileWriter
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


def general_summary(results: list[Student], output_path: str, save_as_txt: bool, save_as_pdf: bool,
                    display_summary: bool, txt_writer: FileWriter, pdf_writer: FileWriter) -> Optional[str]:
    summary = f'*** Created at: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
    for student in results:
        summary += student.display_student_info() + '\n'
        summary += '_ _ _\n'

    if save_as_txt:
        txt_writer.write(summary, output_path)
    if save_as_pdf:
        pdf_writer.write(summary, output_path)
    if display_summary:
        print_to_terminal(summary)

    return summary if (save_as_txt or save_as_pdf) else None


def print_to_terminal(summary: Optional[str]) -> None:
    print(summary)
