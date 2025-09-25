# Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Change Items
# Add Items
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# To add more than one item to a set use the update() method.
thisset = {"apple", "banana", "cherry"}
thisset.update(["orage", "mango", "grapes"])
print(thisset)

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print( len(thisset) )

# Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)

# Set Methods
# add()-Adds an element to the set
# clear()-Removes all the elements from the set
# copy()-Returns a copy of the set
# difference()-Returns a set containing the difference between two or more sets
# difference_update()-Removes the items in this set that are also included in another, specified set
# discard()-Remove the specified item
# intersection()-Returns a set, that is the intersection of two other sets
# intersection_update()-Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()-Returns whether two sets have a intersection or not
# issubset()-Returns whether another set contains this set or not
# issuperset()-Returns whether this set contains another set or not
# pop()-Removes the specified element
# symmetric_difference()-Returns a set with the symmetric differences of two sets
# symmetric_difference_update()-Inserts the symmetric differences from this set and another
# union()-Return a set containing the union of sets
# update()-Update the set with the union of this set and others