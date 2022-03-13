x,y,z = 'Ishaan','Cheeku','Nidhi'

print(f'{x} loves {y} and {z}')

# DECLARING GLOBAL VARIABLE IN FUNCTION

def printProps():
    global name 
    name = 'Michael';
    return name;

name_printer = printProps()

print(name_printer)


# PRINT LENGTH OF STRING/ARRAY

print(len(x))

for letter in x:
    print(letter)

statement = 'I am checking if word is in this statement or not'

if 'checking' in statement:
    print('Yes')

if 'hero' not in statement:
    print('Woops')

# SLICING STRING
print(x[2:])
print(x[:3])
print(x[2:5])

# TO TRIM WHITESPACES BEFORE OR AFTER TEXT
check = ' Hello '
print(check.strip())

# THERE IS ALSO A SPLIT METHOD SIMILAR TO JAVASCRIPT
print(statement.split(' '))

