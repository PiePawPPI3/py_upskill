# main.py
from functions.methods import read_the_file, process_the_content, print_results


def main():
    file_path = "resources/grades1.txt"
    lines = read_the_file(file_path)
    results = process_the_content(lines)
    print_results(results)


if __name__ == "__main__":
    main()
