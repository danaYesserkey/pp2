import re

# 1. 
def match_a_followed_by_bs(string):
    pattern = r'^ab*$'
    return bool(re.match(pattern, string))

print("1.")
print(match_a_followed_by_bs("a"))
print(match_a_followed_by_bs("ab"))
print(match_a_followed_by_bs("abb"))
print(match_a_followed_by_bs("abbb"))
print(match_a_followed_by_bs("b"))
print()

# 2.
def match_a_followed_by_2_3_bs(string):
    pattern = r'^ab{2,3}$'
    return bool(re.match(pattern, string))

print("2.")
print(match_a_followed_by_2_3_bs("abb"))
print(match_a_followed_by_2_3_bs("abbb"))
print(match_a_followed_by_2_3_bs("abbbb"))
print(match_a_followed_by_2_3_bs("ab"))
print()

# 3.
def find_lowercase_underscore_sequences(string):
    pattern = r'\b[a-z]+_[a-z]+\b'
    return re.findall(pattern, string)

print("3.")
print(find_lowercase_underscore_sequences("hello_world_"))
print()

# 4.
def find_upper_then_lowercase_sequences(string):
    pattern = r'\b[A-Z][a-z]+\b'
    return re.findall(pattern, string)

print("4.")
print(find_upper_then_lowercase_sequences("Hello World"))
print()

# 5.
def match_a_anything_ending_b(string):
    pattern = r'^a.*b$'
    return bool(re.match(pattern, string))

print("5.")
print(match_a_anything_ending_b("axb"))
print(match_a_anything_ending_b("a123b"))
print(match_a_anything_ending_b("ab"))
print(match_a_anything_ending_b("a123"))
print()

# 6.
def replace_space_comma_dot_with_colon(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)

print("6.")
print(replace_space_comma_dot_with_colon("Hello, world."))
print()

# 7.
def snake_to_camel(string):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), string)

print("7.")
print(snake_to_camel("hello_world_"))
print()

# 8.
def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

print("8.")
print(split_at_uppercase("HelloWorld"))
print()

# 9.
def insert_spaces_before_capitals(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

print("9.")
print(insert_spaces_before_capitals("HelloWorld"))
print()

# 10.
def camel_to_snake(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

print("10.")
print(camel_to_snake("HelloWorld"))
print()
