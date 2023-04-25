# Dictionary is collection which is unordered, changeable and do not allow duplicates.

thisDict = {
    "A": 1,
    "B": 2,
    "C": 3
}

print(thisDict)

# duplicates not allowed
thisDict = {
    "A": 1,
    "B": 2,
    "C": 3
}

print(thisDict.items())

# length of the dict
print(len(thisDict))

# dict constructor
thisDictConst = dict(name="Biswajit", company="CGI")
print(thisDictConst)

# get all the keys of the dict
print(thisDict.keys())

# add a new item to the original
thisDict["D"] = 5
print(thisDict)

# get values
print(thisDict.values())

# check if a key exists
if "A" in thisDict:
    print("Yes")

# update dictionary
thisDictConst.update({"company": "Wipro"})
print(thisDictConst)

# remove items
thisDict.pop("D")
print(thisDict)

# remove the last inserted item
thisDict.popitem()
print(thisDict)

# loop through the dict
for x in thisDict:
    print(thisDict[x])
