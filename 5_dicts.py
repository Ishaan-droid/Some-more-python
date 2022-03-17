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