# Lists are ordered, changeable, and allow duplicates
# List items are
# List can contain mix of data types

thislist = ["A", "B", "C", "C"]
print(thislist)

thislist[1] = "D"
print(thislist)

print(len(thislist))

# list constructor

aList = list(("apple", "banana", "cherry"))
print(aList)

# append elements to the list
aList.append("grapes")
print(aList)

# add a list to a list
thislist.append(aList)
print(thislist)

# remove all the elements from the list
aList.clear()
print(aList)

# extends the list to another list
bList = ["Hi"]
thislist.extend(bList)
print(thislist)

# inserts an elements at the specified position
thislist.insert(2, 3)
print(thislist)

# removes an element at the specified position
thislist.pop(2)
print(thislist)

# removes the first item with the specified value
thislist.remove('C')
print(thislist)

# sort the list
print(thislist.sort())
