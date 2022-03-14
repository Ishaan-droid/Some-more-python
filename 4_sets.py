# SETS IN PYTHON. DUPLICATES ARE NOT ALLOWED IN SETS. WE CAN ONLY ADD OR REMOVE ITEMS FROM SET

mySet = {'apple','banana','cherry'}

for s in mySet:
    print(s)

print('banana' in mySet)

# ADD ITEMS IN SET

mySet.add('Grapes')

# MERGIN 2 SETS 

mynewSet = {'Mangoes','Jackfruit'}

mySet.update(mynewSet);

# REMOVE ITEM FROM SET. IF ITEM DOES NOT EXIST IN SET 'REMOVE' WILL RAISE AN ERROR
# BUT 'DISCARD' WON'T RAISE ANY ERROR

mynewSet.remove('Jackfruit')

print(mySet)

# READ SETS IF NEEDED
