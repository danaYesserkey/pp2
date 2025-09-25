# Python Tuples
thistuple = ("apple", "banana", "cherry")

# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print( thistuple[1] )

# Change Tuple Values
thistuple = ("apple", "banana", "cherry")
#thistuple[1] = "blackcurrant"

# The values will remain the same:
print(thistuple)

# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print( len(thistuple) )

# Add Items
thistuple = ("apple", "banana", "cherry")
#thistuple[3] = "orange" # This will raise an error
print(thistuple)

# Remove Items
thistuple = ("apple", "banana", "cherry")
print(thistuple) # this will raise an error because the tuple no longer exists

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Tuple Methods
# count()-Returns the number of times a specified value occurs in a tuple
# index()-Searches the tuple for a specified value and returns the position of where it was found

# ex
fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(len(fruits))

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])