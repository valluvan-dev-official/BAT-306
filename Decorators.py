# Decorators :

"""
    - Decorators are a powerful and flexible feature that allows you to modify or extend the behavior of a functions or classes.
    
    - Add Functionality or modify their behaviour  without changing their code directly.

definition :

    - A decorator is a high-order function that allows a function or class as an argument,add some functionality or modifies it and returns a new function or class.

    - Decorators are commonly used for logging and timing functions, authentication and authorization caching
        modifying function behaviour dynamically based on conditions.
"""


"""
def Outer_funtcion(func):  # functions as a Argument


    def Innerfunction():

        print(" ======= Hello All..! ======== ")

        print(" ======= Welcome to BTREE Systems ======== ")

        func()

        print(" ======== Thankyou For your Presence ========= ")

    return Innerfunction  # function  return another function

        


@Outer_funtcion  # function decorate with decorators
def myfun():

    print("This is Python Class")


# Outer_funtcion(myfun)

myfun()

"""