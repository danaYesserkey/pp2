def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"error {e}")
        return 0

filename = input("filename ")
line_count = count_lines(filename)
print(f"'{filename}' has {line_count} lines")
