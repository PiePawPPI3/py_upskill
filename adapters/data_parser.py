import datetime


class EmptyFileError(Exception):
    pass


def read_scores(file_path: str) -> list[dict[str, list[float]]]:
    with open(file_path, 'r') as file:
        data = file.readlines()

    if not data:
        raise EmptyFileError()

    results = []

    for line in data:
        fields = line.strip().split(',')
        username = fields[0]
        scores = []

        for score in fields:
            try:
                score_value = float(score.strip().replace(',', '', 1))
                scores.append(score_value)
            except ValueError:
                pass

        results.append({'username': username, 'scores': scores})

    return results


def display_scores(results: list[dict[str, float]]) -> None:
    print("*** Created at :", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    for result in results:
        print('User:', result['username'])
        print('Scores:', result['scores'])
        print('Average:', result['average'])
        print('_ _ _')
