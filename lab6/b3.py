def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

test_strings = ["hello", "mam"]

for string in test_strings:
    result = is_palindrome(string)
    print(f"'{string}' palindrome is {result}")
