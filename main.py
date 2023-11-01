# main.py
from adapters.data_parser import read_scores, display_scores
from ports.custom_errors import CustomErrors


def main():
    file_path = "resources/grades1.txt"

    try:
        lines = read_scores(file_path)
        display_scores(lines)

    except CustomErrors.FileNotFound:
        print('File not found.')
    except CustomErrors.BinaryFileError:
        print('Decode Error UTF-8.')
    except CustomErrors.AccessDeniedError:
        print('OSError: Access to the file is denied.')
    except CustomErrors.EmptyFileError:
        print('File is empty.')
    except CustomErrors.UnsupportedFileFormatError:
        print('Not supported file type.')
    except CustomErrors.InvalidGradeError:
        print('Grades beyond the range 1-6')
    except CustomErrors.DataProcessingError:
        print('Data processing error')


if __name__ == "__main__":
    main()
