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


