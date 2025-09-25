# Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# The for loop does not require an indexing variable to set beforehand.

for x in "banana":
  print(x)
# The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# The continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# The range() Function
for x in range(6):
  print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)


for x in range(2, 30, 3):
  print(x)
# Else in For Loop

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass
