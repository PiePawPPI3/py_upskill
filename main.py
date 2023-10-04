# main.py
from adapters.data_parser import read_scores, display_scores, EmptyFileError
from busines_logic.calculate_averages import prepare_statistics
from busines_logic.student import Student

def main():
    file_path = "resources/grades1.txt"

    try:
        lines = read_scores(file_path)
        results = prepare_statistics(lines)
        display_scores(results)
    except EmptyFileError:
        print('File is empty.')
    except FileNotFoundError:
        print('File not found.')


if __name__ == "__main__":
    main()
