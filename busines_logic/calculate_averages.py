def preparing_statistics(lines: list[dict]) -> list[dict]:
    results = []
    for line in lines:
        username = line['username']
        scores = line['scores']
        average = round(calculate_average(scores), 1)
        results.append({'username': username, 'scores': scores, 'average': average})
    return results


def calculate_average(scores: list[float]) -> float:
    if scores:
        return sum(scores) / len(scores)
    else:
        return 0
