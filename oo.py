''' 
Combine data and functionality and wrap it inside something called an object.
This is called the object orientated programming paradigm. When writing real
world problems it is easier to follow this programming technique as it better 
represents real things through classes/objects. A class creates a new type
where objects are instances of the class.

Immutable vs Mutable
----------------------
String is immutable
i.e. strings cannot be altered. When you alter a string (by adding to it for example),
you are actually creating a new string.

But StringBuilder is not immutable (rather, it is mutable)
so if you have to alter a string many times, such as multiple concatenations, then use
StringBuilder.

In Python:
Python represents all its data as objects. Some of these objects like lists and dictionaries
are mutable, meaning you can change their content without changing their identity. Other objects 
like integers, floats, strings and tuples are objects that can not be changed. An easy way to understand 
that is if you have a look at an objects ID.
'''


# pass is an empty block of code
# this will ouput the ID of the object
class Person:
    pass 

p = Person()
print(p)


class Animal:
    def speak(self):
        print('meow rawr')

a = Animal()
a.speak()


# explanation of the self keyword
class Business:
    bankrupt = False
    def newbusiness(self):
        if self.bankrupt == False:
            print("new business opened")



# By default a new object will have it's bankrupt field set to false
# The self keyword is the same as the this keyword in C#
# self.bankrupt vs this.bankrupt or this->bankrupt

b = Business()
b.newbusiness()


# explanation of the __init__ keyword
# The init keyword is run as soon as an object of a class is
# instantiated. This will take care of any initialization you
# want to do with your object. 

class Person:
    def __init__(self,name):
        self.name = name
    
    def greeting(self):
        print('hello ' , self.name)

g = Person('Gar')
g.greeting()

# er = Person() error: expects a parameter - name

class County:
    name = ''
    population = 0

    def __init__(self,name,population):
        self.name = name
        self.population = population
        print("Initializing {}".format(self.name))


    def addPerson(self):
        self.population += 1
    

    def display(self):
        print("{} has a population of {}".format(self.name, self.population))


c = County('Ireland', 6000000)
c.addPerson()
c.display()


# Polymorphism in Python
class Animal:
    def __init__(self,name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
    
    def display(self):
        print('{} is {} years old, weighs {} pounds and is {}'.format(self.name, self.age,self.weight, self.color))

class Cat(Animal):
    edible = False
    def __init__(self, name,age, weight, color, sound, edible):
        Animal.__init__(self,name,age,weight, color)
        self.sound = sound
        self.edible = edible
    
    def display(self):

        isedible = ""

        Animal.display(self)
        if self.edible == True: isedible = "is edible"
        else: "is not edible"
        print('he {} and '.format(self.sound), isedible)

mycat = Cat("Brendan", 4, "3", "orange", "meow", True)
mycat.display()