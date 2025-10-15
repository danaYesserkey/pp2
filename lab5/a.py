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