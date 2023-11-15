# main.py
from adapters.data_parser import read_scores, display_scores
from ports.data_parser import UnsupportedFileFormatError, FileNotFound, AccessDeniedError, BinaryFileError, \
    EmptyFileError, InvalidGradeError, DataProcessingError, UnknownError


def main():
    file_path = "resources/grades1.txt"

    try:
        lines = read_scores(file_path)
        display_scores(lines)

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


if __name__ == "__main__":
    main()
