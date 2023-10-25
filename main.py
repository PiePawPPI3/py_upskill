# main.py
from adapters.data_parser import read_scores, display_scores, EmptyFileError, UnsupportedFileFormatError, \
    AccessDeniedError, InvalidGradeError, DataProcessingError


def main():
    file_path = "resources/grades1.txt"

    try:
        lines = read_scores(file_path)
        display_scores(lines)

    except FileNotFoundError:
        print('File not found.')
    except AccessDeniedError:
        print('Access denied to the file.')
    except EmptyFileError:
        print('File is empty.')
    except UnsupportedFileFormatError:
        print('Not supported file type.')
    # except InvalidGradeError:
    #     print('Grades beyond the range 1-6')
    # except DataProcessingError as e:
    #     print(f"Data processing error: {e}")


if __name__ == "__main__":
    main()
