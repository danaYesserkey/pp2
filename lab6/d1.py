import os

def list_contents(path):
    if not os.path.exists(path):
        print(f"'{path}' not exist.")
        return
    
    print(f"\nfiles in '{path}'")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in files:
        print(file)
    
    print(f"\n'{path}':")
    all_items = os.listdir(path)
    for item in all_items:
        print(item)
specified_path = " "
list_contents(specified_path)


# print(f"directories '{path}':")
# directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
# for dir in directories:
# print(dir)
    