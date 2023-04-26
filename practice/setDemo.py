# A set is unchangeable, unordered and unindexed. Duplicates not allowed.

mySet = {"Apple", "Banana", "Cherry"}

# access set items.
for x in mySet:
    print(x)

# check if present.
print("Banana" in mySet)

# add item to the set
mySet.add("Watermelon")
print(mySet)

# remove items from set.
mySet.discard("Banana")
print(mySet)

# difference between remove and discard??
mySet.remove("A")
print(mySet)