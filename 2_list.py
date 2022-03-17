# LIST IN PYTHON

thisList = ['Apple','Banana','Orange','Grapes','Mangoes','Kiwi']

print(thisList[1])
print(thisList[-2])
print(len(thisList))
print(thisList[2:5])
print(thisList[-4:-1])

if 'Banana' in thisList:
    print('Yes, Banana is present im the list.')

if 'Berries' not in thisList:
    print('Berries are not in the list.')

thisList[1] = 'Strawberries'
thisList.insert(2,'Blueberries')
thisList.append('Jackfruit')
thisList.reverse()

print(thisList)

regions = ['Africa','America','Asia','Europe']

regions.extend(thisList)
regions.remove('America')

# FOR POP DEFAULT IS LAST INDEX
regions.pop(1)
regions.clear()

print(regions)

for items in thisList:
    print(items)

for i in range(len(thisList)):
    print(i)

prices = [12,56,47,4,86,45,678,34221]

prices.sort()
prices.sort(reverse=True)

# SORTED METHOD IS USED TO SORT MAPS AND DICT; sorted(list(set(arr)))
# sorted(iterable, key, reverse=True) => True is for descending order

print(prices)

newPrices = prices.copy()

print(newPrices.count(4))