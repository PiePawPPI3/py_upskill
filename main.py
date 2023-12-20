from adapters.data_parser import read_scores
from adapters.data_saver import TxtWriter, HtmlWriter, FileWriter, TerminalPrinter
from ports.data_parser import (
    UnsupportedFileFormatError, FileNotFound, AccessDeniedError, BinaryFileError,
    EmptyFileError, InvalidGradeError, DataProcessingError, UnknownError, FileSaveError
)


def save_summary(summary: list[dict], writers: list[FileWriter]) -> None:
    for writer in writers:
        writer.write(summary)


def main():
    file_path = "resources/grades1.txt"
    output_path = "outputs/"

    save_as_txt = True
    save_as_html = True
    display_summary = True

    try:
        students = read_scores(file_path)
        student_info_list = [student.get_student_info() for student in students]

        writers = []
        if save_as_txt:
            txt_writer = TxtWriter(output_path)
            writers.append(txt_writer)

        if save_as_html:
            html_writer = HtmlWriter(output_path)
            writers.append(html_writer)

        if display_summary:
            terminal_printer = TerminalPrinter()
            terminal_printer.write(student_info_list)

        save_summary(student_info_list, writers)

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
