# Ineritance :


# 1. Single Inheritance :

"""
    A child class inherits from one parent class.
"""
# Example :

"""
class Father: #Parent Class

    name = "John"

    def Car(self):

        print("Father's Car")


# Anbu = Father()

# Anbu.Car()


class Son(Father): # Child class

    my_name = "David"

    def Bike(self):

        print("Son's Bike")



Varun = Son()

Varun.Bike()

Varun.Car()

print(Varun.name)

"""

# Multiple Inheritance :


"""
    A child class inherits from multiple parent classes.
"""

# Example :


"""
class Father: # Parent Class or Base Class

    name = "John"

    def Car(self):

        print("Father's Car")


class Mother: # Parent Class

    name = "Jane"

    def Van(self):

        print("Mother's Van")


class Son(Father, Mother): # Child class or Derived Class

    my_name = "David"

    def Bike(self):

        print("Son's Bike")


Varun = Son()

Varun.Bike()

Varun.Car()

Varun.Van()

print(Varun.name)

"""

# Multi-level Inheritance :

"""

- involve a chain of inheritance Where a child class becomes a parent for another class

"""
# Example :

"""
class Grandpa: # Parent Class

    name = "Grandpa"

    def House(self):

        print("Grandpa's House")


class Father(Grandpa): # Child class

    name = "John"

    def Car(self):

        print("Father's Car")


class Son(Father): # Child class

    my_name = "David"

    def Bike(self):

        print("Son's Bike")


Varun = Son()

Varun.Bike()

Varun.Car()

Varun.House()

print(Varun.name)

"""

# Hierarchical Inheritance :

"""
    Hierarchical Inheritance Occurs when multiple child classes inherit from a single parent class.
"""
# Example :

"""
class Father:

    name = "John"

    def Car(self):

        print("Father's Car")



class Son(Father):

    my_name = "David"

    def Bike(self):

        print("Son's Bike")


class Daughter(Father):

    my_name = "Emma"

    def Scooter(self):

        print("Daughter's Scooter")



Arun = Son()

Arun.Bike()

Arun.Car()


Tina = Daughter()

Tina.Scooter()

Tina.Car()

"""

# Hybrid Inheritance :

"""
    - Combines multiple types of inheritance in a single Program

"""

# example :

"""
class Grandfather:

    def House(self):

        print("Grandfather's House")


class Father(Grandfather):

    def Car(self):
        print("Father's Car")


class Son(Father):

    def Bike(self):
        print("Son's Bike")


class Daughter(Father):

    def Scooter(self):
        print("Daughter's Scooter")

"""

# Try it :


class a:
    ...

class b:
    ...

class c(a):
    ...

class d(a,b):
    ...

class e(a):
    ...

class z(d):
    ...
