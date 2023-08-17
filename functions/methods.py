from typing import List


def read_the_file(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
        if data:
            print('file_content:')
            for line in data:
                process_the_content(line.strip())
        else:
            print('file_is_empty.')


def calculate_average(scores: List[float]):
    if len(scores) > 0:
        return sum(scores) / len(scores)
    else:
        return 0


def print_user_average_score(username: str, average: float) -> None:
    print(f'User {username} has average: {average:.2f}')


def process_the_content(line: str) -> None:
    fields = line.strip().split(',')
    username = fields[0]
    scores = [float(score) for score in fields[1:]
              if score.strip().replace(',', '', 1).isdigit()]
    average = calculate_average(scores)

    print_user_average_score(username, average)
