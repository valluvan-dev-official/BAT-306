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

"""
def add(x,y):

    z = x + y
    return z


a = 50
b = 100

print(add(10,20))

print(add(a,b))

"""


# Example :

"""
def marriage(bride,groom):

    print(bride," Weds ", groom)



marriage("Jothika","Surya")

marriage("Anushka","Virat")

"""


# Arguments :

"""
    - information can be passed into function is called as a arguments

    dont's :

        - function must be called with the correct number of arguments

There are four types of arguments in Python:

    1. Positional Arguments
    2. Arbitrary Arguments
    3. Keyword Arguments
    4. Arbitrary Keyword Arguments


"""

# Arbitrary Arguments :

"""
    if the number of arguments is unknown add * before the parameter
    use * for variable-length arguments
"""

"""
def greeting_msg(*names):

    for name in names:

        print(f"hello, {name} welcome to our Resort ")



greeting_msg("Deepika","Rajesh","Kumar","Arun")


# greeting_msg("Rajesh")

"""


# Keyword Arguments :

"""
   Arguments passed as key = value 
   this way the order of the arguments does not match 

"""

"""
def myfun(name, age):

    print(f"{name} is {age} years old")


myfun(age=30, name="Rajesh")

myfun(name="John", age=25)

"""

# Arbitrary Keyword Arguments :

""""
 use ** for variable-length keyword arguments

 if the number of keyword arguments is unknown add double ** before  the parameter

"""

# Example :

"""
def info(**details):

    for key,value in details.items():
        print(f"{key} : {value}")



info(name = "John", age=25)

info(age = 24, name = "Amar")

"""

# Default Argumetns :

"""
    Provide default values.
    if we call the function without argument it uses the default value.

"""
# Example :

"""
def myfun(name = "John"): 

    print("welcome ", name) 
    
    
myfun("Deepika")
myfun()
myfun("Arun")

""" 

# Function Returning Multiple Values :

# Example without multiple values :
"""
def myfun():
    
    a = 20
    b = 30 
    c = a + b

    # return "Welcome to India"

    return c

print(myfun())

"""

# example with multiple vaues :

"""def calculate(a,b):

    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    return addition, subtraction, multiplication, division

# print(calculate(10,5))

add,sub,mul,div = calculate(10,5) # (15,5,50,2.0)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
"""

# Example :

"""
def myfun():

    print("Deepika")

    return "Welcome to India"


# print(myfun())

text = myfun()

print(text)

"""

# ========= Scope of Variables =========

"""
    a variable scope specifies the region where we can access a variable.

    Based on the Scope, Python variablesinto three types :

        1. Global scope
        2. Local scope
        3. Non local scope

"""

# Global Scope :

"""
    - a variable that is defined ouside a function has a global scope
    - it can be accessed inside and outside the function

"""

"""
name = "Amar"


def myfun():

    print("Inside the Function",name) 


print("Outside the function",name)

myfun()

"""


# Local Scope :

"""
    a variable that is defined inside a function has a local scope
    it can only be accessed inside that function

"""
# Example :

"""
def myfun():

    name = "Vijay"

    print("Inside the Function", name)


myfun()

print("Outside the Function", name)

"""

# Non Local Scope :

"""
    - a variable that is defined in the outer function but not in the global scope is called non local variable
"""

# Example :

"""
def myfun():

    name = "Thalapathy"

    def greet():

        print("Hello", name)

    return greet()


myfun()

"""


# ============ Lambda Function ============

"""
    a lambda function is a small anonymous function
    it can take any number of arguments, but can only have one expression
    it is defined using the lambda keyword
    it is used to define small functions


    Syntax :

        lambda arguments : expression


        lambda : keyword to define  a lambda function
        arguments : input parameters for the function
        expression : a single expression to be evaluated and returned

"""


# x = lambda a,b : (a * b) + (a / b)

# print(x(10,2))


# ==============================================

# Map :

"""

    oru function ah ella elements kku apply pannum

    
    Syntax :

        map(function, iterable)

"""

# example :

# numbers = [1,2,3,4]

# nums = [5,6,7,8]

"""
def square(x):

    return x * x

result = map(square, numbers)

print(list(result))

"""

# Using map in Lambda :

# result = tuple(map(lambda x : x * x , numbers))

# print(result)


# =====================

# filter()

"""
Syntax :

    filter(function, iterable)

    function -> True / False Return Pannum
    function = None , Truthy elements return pannum


Truthy Elements :

    - Elements that are considered True in a boolean context
    - Examples: Non-empty strings, non-zero numbers, non-empty lists, etc.

Falsy Elements:

        - Elements that are considered False in a boolean context
        - Examples: Empty strings, zero, None, empty lists, etc.

"""

# example :

"""
numbers = [10,15,20,25,30]

even_numbers = filter(lambda x : x % 2 == 0, numbers)

print(list(even_numbers))

"""

# Example :

"""
words = ["Hi",""," ","Welcome","","Python"]

result = filter(None, words)

print(list(result))

"""

# Reduce :

from functools import reduce 

"""
reduce(function,iterable,initializer)

function(acc,cur)

"""

#nums = [1,2,3,4]


# result = reduce(lambda acc, x : acc + x, nums)


"""
==> 0 + 1 = 1

acc = 1

=> 1 + 2 = 3

acc = 3 

=> 3 + 3 = 6

acc = 6

=> 6 + 4 = 10

"""

# print(result)



# ======== Lambda function sorting ========


"""
students = [("John", 25), ("Jane", 22), ("Dave", 23), ("Alice", 24)]

# Sort by age :

sorted_students = sorted(students,key = lambda x : x[1])

print(sorted_students)

"""

# ======= Conditional Expression in Lambda ========

"""
Syntax :

    lambda arguments : value_if_true if condition else value_if_false

"""

# Check Even or Odd :

result = lambda x : "Even" if x % 2 == 0 else "Odd"

num = int(input("Enter Num : "))

print(result(num))








