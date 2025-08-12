# Functions in Python :

"""
What are Python Functions?

    A function is a block of organized, reusable code designed to perform a specific task or set of tasks.
    Functions allow for better modularity and code reuse in python


    set of instructions called as a functions
    a reusable block of code that performs a specific task or set of tasks.


Types of Functions :

    1. built-in functions
    2. user-defined functions
    3. lambda functions


1. Built-in Functions :

    len()
    print()
    input()
    append()
    extend()
    pop()
    remove()

2. User - Defined Functions :

    There are two types of concepts :

        1. void functions - without return

                - it returns nothing

                1. with Argument
                2. without Argument

        2. Non void functions - with return

                - it has something to return

                1. with Argument
                2. without Argument


Syntax :

    def function_name(parameters):
        # function body
        return value



    def - Keyword for declare a function

    function_name = name of the function

    parameters = optional, it is variable that is passed in to the function
"""


# function definition

"""
def myfun():

    print("Hello, World!")


myfun()
myfun()
myfun()
myfun()
myfun()
myfun()

"""


# Void Functions :

# with Argument :

"""
def add(a,b):

    c = a + b
    print(c)



add(10,20) 

add(100,200)

add(50,60)

print(add(3500,3500))

"""

# With out Argument :

"""
def add():

    a = int(input("Enter num  : "))
    b = int(input("Enter num  : "))
    c = a + b
    print(c)


add()

"""


# Non Void Functions :

# without Argument

"""
def add():

    a = 20
    b = 30
    c = a + b
    # return c
    print(c)

# print(add())

num = add()
print(num)

"""

# With Argument :

def add(x,y):

    z = x + y
    return z


a = 50
b = 100

print(add(10,20))

print(add(a,b))