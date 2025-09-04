
# Class:

"""
    Class is a blueprint for creating objects 

    it defines attributes(Variables) and methods(Functions)that the objects 
    of the class will have

"""

"""
class Car:

    Brand = "BMW"  # Attributes
    Year = 2024

    def Drive(self):    # Methods
        print("The car is driving.") 

"""

# Object :

"""
    An Object is an Instance of a Class

    its Created Using the Class as a Template and Has it's Unique data

"""

"""
my_car = Car()

# print(my_car.Brand)
# print(my_car.Year)
# my_car.Drive()


Deepika_car = Car()

print(Deepika_car.Brand)
print(Deepika_car.Year)
Deepika_car.Drive()

"""



# Person :
   
"""
class Person:

    Name = "John Doe"  # Attributes
    Age = 30


    def info(self,Name,Age):
        # print("my name is Hello","and my age is 24")

        print(f"My name is {Name} and my age is {Age}")


# person_info = Person()

# print(person_info.Name)


a = Person()

a.info("Deepika", 28)


"""

# Constructor :

class Person:

    Course = "Python"

    def __init__(self,Name,Age,Address):

        self.my_name = Name
        self.my_age = Age
        self.my_address = Address


    def info(self):

        # print(f"My course is {self.Course}")
        print(f"My name is {self.my_name}, my age is {self.my_age} and my address is {self.my_address} and My course is {self.Course}")


    def display_info(self):

        print(f"Name: {self.my_name}")
        print(f"Age: {self.my_age}")
        print(f"Address: {self.my_address}")
        print(f"Course: {self.Course}")


Arun = Person("Arun",25,"Chennai")
# print(Arun.my_name)
# print(Arun.my_age)
# print(Arun.my_address)
# Arun.info()
x = "Deepika"
Deepika = Person(x,28,"Bangalore")
Deepika.info()
Deepika.display_info()






