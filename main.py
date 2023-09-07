# main.py
from adapters.data_parser import read_scores, display_scores
from busines_logic.calculate_averages import preparing_statistics


def main():
    file_path = "resources/grades1.txt"
    lines = read_scores(file_path)
    results = preparing_statistics(lines)
    display_scores(results)


if __name__ == "__main__":
    main()
