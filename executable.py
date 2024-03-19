

import os

def get_next_filename():
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    i = 1
    while True:
        output_filename = f"output_{i}.txt"
        output_path = os.path.join(exe_dir, output_filename)
        if not os.path.exists(output_path):
            return output_path
        i += 1

def create_text_file():
    message = "This is a test message created by the executable file."
    output_path = get_next_filename()
    with open(output_path, "w") as file:
        file.write(message)

if __name__ == "__main__":
    create_text_file()
