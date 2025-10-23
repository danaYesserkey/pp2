import os

def check_path(path):
    if os.path.exists(path):
        print(f"'{path}' exists.")
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"directory '{directory}'")
        print(f"filename portion '{filename}'")
    else:
        print(f"'{path}' not exist.")

path = input("path ")
check_path(path)