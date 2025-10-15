import re
r = open("a.txt", "r")
content = r.read()
r.close()

i = re.search("ИТОГО:", content).end()
i += 1
total = ""
while i < len(content) and content[i] != '\n':
    total += content[i]
    i += 1
print("Total:", total)

i = re.search("Время: ", content).end()
date = ""
while i < len(content) and content[i] != '\n':
    date += content[i]
    i += 1
print("Date:", date)

# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
print("\n1. Match 'a' followed by zero or more 'b's:")
pattern1 = r'ab*'
sample1 = "ab abb a b abc"
matches1 = re.findall(pattern1, sample1)
print("Sample:", sample1)
print("Matches:", matches1)

matches1_txt = re.findall(pattern1, content)
print("In a.txt (first 5):", matches1_txt[:5])

# 2. Write a Python program that matches a string that has an 'a' followed by one or more 'b''s.
print("\n2. Match 'a' followed by two to three 'b's:")
pattern2 = r'ab{2,3}'
sample2 = "abb abbb abbbb a abc"
matches2 = re.findall(pattern2, sample2)
print("Sample:", sample2)
print("Matches:", matches2)
matches2_txt = re.findall(pattern2, content)
print("In a.txt:", matches2_txt)

# 3. Write a Python program to find sequences of lowercase letters joined with a underscore.
print("\n3. Find sequences of lowercase letters joined with underscore:")
pattern3 = r'\b[a-z]+_[a-z]+\b'
sample3 = "hello_world test_case UPPER lower_upper"
matches3 = re.findall(pattern3, sample3)
print("Sample:", sample3)
print("Matches:", matches3)
matches3_txt = re.findall(pattern3, content)
print("In a.txt:", matches3_txt)

# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
print("\n4. Find sequences of one uppercase letter followed by lowercase letters:")
pattern4 = r'\b[A-Z][a-z]+\b'
sample4 = "Hello world TestCase UPPER"
matches4 = re.findall(pattern4, sample4)
print("Sample:", sample4)
print("Matches:", matches4)
matches4_txt = re.findall(pattern4, content)
print("In a.txt (first 10):", matches4_txt[:10])

# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
print("\n5. Match 'a' followed by anything, ending in 'b':")
pattern5 = r'a.*b$'
sample5 = "ab a123b axb a b abc"
matches5 = [s for s in sample5.split() if re.match(pattern5, s)]
print("Sample:", sample5)
print("Matches:", matches5)
lines = content.split('\n')
matches5_txt = [line for line in lines if re.match(pattern5, line.strip())]
print("Matching lines in a.txt:", matches5_txt[:3])

# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
print("\n6. Replace space, comma, or dot with colon:")
pattern6 = r'[ ,.]'
sample6 = "Hello, world. Test case."
result6 = re.sub(pattern6, ':', sample6)
print("Sample:", sample6)
print("Result:", result6)
sample_line = "Натрия хлорид 0,9%, 200 мл, фл"
result6_txt = re.sub(pattern6, ':', sample_line)
print("Sample from a.txt:", sample_line)
print("Result:", result6_txt)

# 7. Write a python program to convert snake case string to camel case string.
print("\n7. Convert snake case to camel case:")
def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)
sample7 = "hello_world test_case_example"
result7 = snake_to_camel(sample7)
print("Sample:", sample7)
print("Result:", result7)
snake_in_txt = re.findall(pattern3, content)
if snake_in_txt:
    result7_txt = [snake_to_camel(s) for s in snake_in_txt]
    print("Converted in a.txt:", result7_txt)

