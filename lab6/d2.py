import os

def check_access(path):
    if not os.path.exists(path):
        print(f"'{path}' not exist.")
        return
    
    print(f"checking '{path}':")
    print(f"exist {os.path.exists(path)}")
    print(f"readable {os.access(path, os.R_OK)}")
    print(f"writable {os.access(path, os.W_OK)}")
    print(f"executable {os.access(path, os.X_OK)}")

specified_path = "."
check_access(specified_path)