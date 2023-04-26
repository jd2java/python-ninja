# Tuple items are ordered, unchangeable and allow duplicate values.

myTuple = (1, "Orange", "Banana")
print(myTuple)

# length of the tuple.
print(len(myTuple))

# tuple constructor
thisTuple = tuple(("Apple", "Orange"))
print(thisTuple)

# negative indexing access.
print(thisTuple[-1])

# range of indexes
print(thisTuple[1:])

# count tuple.
print(thisTuple.count("Apple"))

# return the first occurance of the value.
print(thisTuple.index("Apple"))