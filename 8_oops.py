class Details:
    def __init__(self,name,age,birth,grade):
        self.name = name
        self.age = age
        self.birth = birth
        self.grade = grade

    def printProps(self):
        return print(f'My name is {self.name} and I am {self.age} years old.')

d = Details('Ishaan',26,1995,'A+')

class PrintBirth(Details):
    def __init__(self,name,age,birth,grade,power):
        super().__init__(name,age,birth,grade)
        self.power = power

    def printProps(self):
        return print(f'My birth is {self.birth} and my power is {self.power}')

d.printProps()