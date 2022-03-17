def printName(name='Cheeka'): # Assigning default value to function
    print(f'My name is {name}.')

printName('Ishaan')

'''
If you do not know how many arguments that will be passed into your function,
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly.
'''

def soManyNames(*names):
    print(f'All the names {names}')

soManyNames('Ishaan','Cheeka','John','Tom')

