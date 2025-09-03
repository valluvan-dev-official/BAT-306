# Method Overloading:


"""
class Calcculator:

    def add(self,a):

        print("Adding:", a)

    def add(self,a,b):

        print("Adding:", a + b)

    def add(self,a,b,c):

        print("Adding:", a + b + c)


obj = Calcculator()

# obj.add(5)

# obj.add(5, 10)

obj.add(5, 10, 15)

"""

# Proper Method Overloading :


"""
class Calculator:

    def add(self,a = 0,b = 0,c = 0):

        print("Adding:", a + b + c)



obj = Calculator()

obj.add(5)

obj.add(5, 10)

obj.add(5, 10, 15)

"""

# Method Overriding :

class Animal:

    def make_sound(self):
        return "Some generic sound"
    

class Dog(Animal):

    def make_sound(self):
        return "Bark"
    

class Cat(Animal):

    def make_sound(self):
        return "Meow"

# Using polymorphism

# animals = Dog()

# print(animals.make_sound())


"""
animal = Animal()
print(animal.make_sound())

animal1 = Dog()
print(animal1.make_sound())

animal2 = Cat()
print(animal2.make_sound())

"""

# animals= [Dog(), Cat(), Animal()]

# for animal in animals: #dog
    
#     print(animal.make_sound())





# Duck Typing :


class Bird:

    def fly(self):
        return "Flapping wings"


class Airplane:

    def fly(self):
        return "Flying with wings"


class Dolphin:

    def swim(self):
        return "Swimming with fins"
    


def Lift_off(data):

    print(data.fly())




Lift_off(Bird())
Lift_off(Airplane())
Lift_off(Dolphin())