def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"written '{filename}' success")
    except Exception as e:
        print(f"error {e}")

data = ["apple", "banana", 42, True]
filename = "list.txt"
write_list_to_file(filename, data)
