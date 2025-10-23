import re

def replace(string):
    pattern = r"^g.*ing$"
    return re.findall(pattern,string)

print(replace("gliding"))

# start at g and end at ing gliding