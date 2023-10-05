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

        username = "Cezary"
        students_list = [student for student in results if student['username'] == username]

        if students_list:
            for student_details in students_list:
                scores = student_details['scores']
                student = Student(username, scores)
                student.display_student_info()

                average = student.calculate_average()
                print('Average for ' + username + ': ' + str(average))
        else:
            print('Student with username' + username + 'does not exist.')

    except EmptyFileError:
        print('File is empty.')
    except FileNotFoundError:
        print('File not found.')


if __name__ == "__main__":
    main()
