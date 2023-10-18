# main.py
from adapters.data_parser import read_scores, display_scores, EmptyFileError


def main():
    file_path = "resources/grades1.txt"

    try:
        lines = read_scores(file_path)
        display_scores(lines)

    except EmptyFileError:
        print('File is empty.')
    except FileNotFoundError:
        print('File not found.')


if __name__ == "__main__":
    main()
