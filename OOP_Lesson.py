class Person:
    species = "homo sapiens" # This is a class attribute, it is shared by all instances of the class. Used for default value for all instances or to track data across instances.
    def __init__(self, name, socialSecurity, salary): # Constructor, runs as soon as an object of a class is instantiated.
        self.name = name #These are all instance attributes
        self.socialSecurity = socialSecurity
        self.salary = salary

    def get_info(self):
        print(f" I'm {self.name}, {self.socialSecurity}, I make {self.salary}.")


# Uses the Class (our 'blueprint') to create objects
p1 = Person('Jill', '069420', 25)
p2 = Person('Jack', '492567', 15)

print(p1.get_info())

# Inheritance: classes can inherit from others so we can make an Airplane class (a child class) from our parent Vehicle class for example.\

class IrishPerson(Person): #Creates a class which inherits from our parent Person class.
    def __init__(self, name, socialSecurity, salary, county):
        '''self.name = name
        self.socialSecurity = socialSecurity
        self.salary = salary''' # instead of copying this info from parent class, use super()
        super().__init__(name, socialSecurity, salary)
        self.county = county

    def get_info(self):
        print(f" I'm {self.name} from {self.county}.")

Sean = IrishPerson('Sean', '069420', 25, 'Fermanagh')
Sean.get_info()

# Polymorphism Example
# Polymorphism is the ability to get a different response despite same class so...
print(p1.get_info())
print(Sean.get_info()) # This is polymorphism