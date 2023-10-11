# main.py
from adapters.data_parser import read_scores, display_scores, EmptyFileError
from busines_logic.calculate_averages import prepare_statistics
from ports.student import Student


def main():
    file_path = "resources/grades1.txt"

    try:
        lines = read_scores(file_path)
        results = prepare_statistics(lines)
        display_scores(results)

        for student_details in results:
            username = student_details['username']
            scores = student_details['scores']
            student = Student(username, scores)
            student.display_student_info()

    except EmptyFileError:
        print('File is empty.')
    except FileNotFoundError:
        print('File not found.')


if __name__ == "__main__":
    main()
