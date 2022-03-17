x = 50
y = 100

if y > x:
    print(f'{y} is greater than {x}')
elif x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} and {y} are equal.')

n = 5

# THERE ARE ALSO BREAK AND CONTINUE STATEMENTS IN WHILE LOOP

while n>0:
    print(n)
    n -= 1

'''
The range() function returns a sequence of numbers, starting from 0 by default,
and increments by 1 (by default), and ends at a specified number.
'''

for k in range(6): # 6 will not be included in the loop
    print(k)

for k in range(2,6):
    print(k)