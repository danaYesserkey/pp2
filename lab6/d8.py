import os

def delete_file(path):
    if not os.path.exists(path):
        print(f"'{path}' not exist.")
        return
    
    if not os.access(path, os.W_OK):
        print(f"no access to '{path}'.")
        return
    
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"File '{path}' deleted ")
        else:
            print(f"'{path}' is not a file")
    except Exception as e:
        print(f"error '{path}': {e}")

file_to_delete = "list.txt"
delete_file(file_to_delete)
