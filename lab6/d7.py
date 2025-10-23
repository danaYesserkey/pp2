def copy_file(source, destination):
    try:
        with open(source, 'r') as src:
            content = src.read()
        with open(destination, 'w') as dest:
            dest.write(content)
        print(f"copied'{source}' to '{destination}' success")
    except FileNotFoundError:
        print(f"source '{source}' not found")
    except Exception as e:
        print(f"error {e}")

source_file = input("filename ")
destination_file = input("destination ")
copy_file(source_file, destination_file)
