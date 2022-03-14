# TUPLES IN PYTHON. TUPLES ARE IMMUTABLE

myTupple = ('Apples','Oranges','Bananas','Cherry','Grapes','Jackfruit')

print(myTupple)

# LENGTH,INDEX,CONVERSION,LOOP ARE SAME AS LIST

# UPDATING IN TUPLE IS NOT POSSIBLE BUT THERE IS A WORK AROUND

newList = list(myTupple)
newList[1] = 'Mangoes'
myTupple = tuple(newList)

(x,y,*veggies) = myTupple

print(veggies)

# LOOP IS SAME LIKE LIST

myTupple2 = (1,2,3)

myTupple3 = myTupple + myTupple2

print(myTupple3)

# COUNT IS ALSO SAME LIKE LIST
