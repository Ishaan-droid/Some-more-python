# DICTONARIES IN PYTHON
thisDict = {
    'brand': 'mercedes',
    'model': 'A-class',
    'year': 1954,
};

print(thisDict['brand'])
print(thisDict.get('brand'))

thisDict['age'] = 24

k = thisDict.keys()
v = thisDict.values()

print(thisDict)

print(sorted(thisDict))

# del thisDict['year']

print(thisDict)

for x in thisDict:
    print(x, thisDict[x])

for x,y in thisDict.items():
    print(x,y)

mydict = thisDict.copy()

print(mydict)
