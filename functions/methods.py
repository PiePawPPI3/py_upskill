# functions/grades1.py

def read_the_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read()
            if data:
                print("file_content: ")
                print(data)
            else:
                print("file_is_empty.")
    except FileNotFoundError:
        print("file_doesnt_exist.")
