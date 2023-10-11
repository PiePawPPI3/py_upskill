from ports.student import Student


def prepare_statistics(lines: list[dict[str, list[float]]]) -> list[dict[str, any]]:
    results = []
    for line in lines:
        username = line['username']
        scores = line['scores']
        student = Student(username, scores)

        results.append({'username': username, 'scores': scores, 'average': student.calculate_average()})
    return results

