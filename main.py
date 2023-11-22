import datetime

from adapters.data_parser import read_scores
from adapters.data_saver import TxtWriter, PdfWriter, FileWriter, TerminalPrinter
from ports.data_parser import (
    UnsupportedFileFormatError, FileNotFound, AccessDeniedError, BinaryFileError,
    EmptyFileError, InvalidGradeError, DataProcessingError, UnknownError, FileSaveError
)
from ports.student import Student


def generate_summary_text(results: list[Student]) -> str:
    summary = f'*** Created at: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
    for student in results:
        summary += student.get_student_info() + '\n'
        summary += '_ _ _\n'
    return summary


def save_summary(summary: str, output_path: str, save_as_txt: bool, save_as_pdf: bool, display_summary: bool,
                 txt_writer: FileWriter,
                 pdf_writer: FileWriter, terminal_printer: FileWriter) -> None:
    if save_as_txt:
        txt_writer.write(summary, output_path)
    if save_as_pdf:
        pdf_writer.write(summary, output_path)
    if display_summary:
        terminal_printer.write(summary)


def main():
    file_path = "resources/grades1.txt"
    output_path = "outputs/"

    save_as_txt = True
    save_as_pdf = False
    display_summary = True

    try:
        lines = read_scores(file_path)
        summary_text = generate_summary_text(lines)
        txt_writer = TxtWriter()
        pdf_writer = PdfWriter()
        terminal_printer = TerminalPrinter()

        save_summary(summary_text, output_path, save_as_txt, save_as_pdf, display_summary, txt_writer, pdf_writer,
                     terminal_printer)

    except FileNotFound:
        print('File not found.')
    except BinaryFileError:
        print('Decode Error UTF-8.')
    except AccessDeniedError:
        print('Access to the file is denied.')
    except EmptyFileError:
        print('File is empty.')
    except UnsupportedFileFormatError:
        print('Not supported file type.')
    except InvalidGradeError:
        print('Grades beyond the range 1-6')
    except DataProcessingError:
        print('Data processing error')
    except UnknownError:
        print('Unknown error encountered')
    except FileSaveError as e:
        print(f'Error occurred while saving the file: {e}')


if __name__ == "__main__":
    main()
