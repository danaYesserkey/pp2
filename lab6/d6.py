import os

def generate_text_files():
    for i in range(26):
        filename = chr(65 + i) + ".txt"
        try:
            with open(filename, 'w') as file:
                file.write(f"file {filename}\n")
            print(f"created {filename}")
        except Exception as e:
            print(f"error {filename}: {e}")

generate_text_files()
