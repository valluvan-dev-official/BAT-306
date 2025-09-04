# abstraction :
"""
    the process of hiding complex implementation details and
exposing only the necessary functionalities or interfaces to the user.

    abstraction is used to hide the internal functionality of the 
function from the users.
    
    the users only interact with basic implementation of the 
function but inner working is hidden

    user is familiar with that " what function does" but they don't know
"how it does".

    we need to import the abc module which provides the base for
defining Abstract Class(ABC)

syntax :
    from abc import ABC,abstractmethod

"""
from abc import ABC, abstractmethod

# Anstract class la What to do nu Declare panrom
# but How to do nu Child class la implement panrom


class Vehicle(ABC): 

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass 


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

obj = Vehicle()
obj.start()
obj.stop()