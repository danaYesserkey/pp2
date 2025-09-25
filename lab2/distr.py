# Dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print (thisdict)

# Accessing Items
x = thisdict["model"]
x = thisdict.get("model")

# Change Values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# Loop Through a Dictionary
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)

# Dictionary Length
print( len(thisdict) )

# Adding Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Removing Items

# The del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# The pop() method removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
#print(thisdict) # this will cause an error because "thislist" no longer exists.

# The clear() keyword empties the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# The dict() Constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)


# Dictionary Methods
# clear()               Removes all the elements from the dictionary
# copy()                Returns a copy of the dictionary
# fromkeys()            Returns a dictionary with the specified keys and values
# get()                 Returns the value of the specified key
# items()               Returns a list containing the a tuple for each key value pair
# keys()                Returns a list containing the dictionary's keys
# pop()                 Removes the element with the specified key
# popitem()             Removes the last inserted key-value pair
# setdefault()          Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()              Updates the dictionary with the specified key-value pairs
# values()              Returns a list of all the values in the dictionary