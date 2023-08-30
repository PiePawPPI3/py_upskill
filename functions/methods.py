def read_the_file(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()

        if not data:
            print('File is empty.')
        return data

    except FileNotFoundError:
        print('File not found.')


def process_the_content(lines: list) -> list[dict]:
    results = []
    for line in lines:
        fields = line.strip().split(',')
        username = fields[0]
        scores = []
        for score in fields:
            try:
                score_value = float(score.strip().replace(',', '', 1))
                scores.append(score_value)
            except ValueError:
                pass

        average = round(calculate_average(scores), 1)
        results.append({'username': username, 'scores': scores, 'average': average})
    return results


def calculate_average(scores: list[float]) -> float:
    if scores:
        return sum(scores) / len(scores)
    else:
        return 0


def print_results(results: list[dict]) -> None:
    for result in results:
        print('User:', result['username'])
        print('Scores:', result['scores'])
        print('Average:', result['average'])
        print('_ _ _')
