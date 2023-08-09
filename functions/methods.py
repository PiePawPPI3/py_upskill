# functions/grades1.py
def read_the_file(file_path):
    with open(file_path, "r") as file:
        data = file.readlines()
        if data:
            print("file_content:")
            for line in data:
                print(line.strip())
                fields = line.strip().split(',')
                username = fields[0]
                scores = [float(score) for score in fields[1:]
                          if score.strip().replace(',', '', 1).isdigit()]
                average = calculate_average(scores)
                print(f"User: {username} has average: {average:.2f}")
        else:
            print("file_is_empty.")


def calculate_average(scores):
    if len(scores) > 0:
        return sum(scores) / len(scores)
    else:
        return 0
