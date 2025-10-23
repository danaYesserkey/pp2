def true(tup):
    return all(tup)

tuples = [
    (True, True, True),
    (True, False, True),
    (1, 2, 3),
    (0, 1, 2),
    ("a", "b", "c"),
    ("d", "b", "a")
]

for tup in tuples:
    result = true(tup)
    print(f"{tup} = {result}")
