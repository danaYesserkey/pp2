# Python If ... Else

#Logical conditions:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200
if b > a:
    print("b is greater than a")


# Elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
a = 200
b = 33
c = 50
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
print("A") if a > b else print("=") if a == b else print("B")

# And
if a > b and c > a:
    print("Both conditions are True")

if a > b or a > c:
    print("At least one of the conditions are True")