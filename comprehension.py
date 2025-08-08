# Types of comprehensions in Python :

"""
    1. List Comprehension
    2. Dictionary Comprehension
    3. Set Comprehension
    
""" 

# List Comprehension :

# numbers = [10,13,15,20,26,30,33,47,50]

# Without Comprehension

"""
even = []

for i in numbers:

    if i % 2 == 0:
        even.append(i)

print(even)

"""

# With Comprehension

"""
Syntax :

    [expression for item in iterables if condition]

Expression :
    
    - This is operator or value you want to include in the new list

Item :

    - it represents each item in the iterables that you want to process

Iterable:

    - the source of data,such us list,tuple,set,dictionary or range from which you want to generate the new list

Condition :

    - This is an optional Filter that determines whether an item should be included in the new list.

    - if the condition is not provided, all items from the iterable will be included in the new list.
"""

# Example :

"""
numbers = [10,13,15,20,26,30,33,47,50]

even = [i for i in numbers if i % 2 == 0]

print(even)

"""

# Nested Loop in Comprehension 


"""
a = [1,2,3,4,5] 

b = [6,7,8,9,10] 

even = [(i,j) for i in a for j in b if i % 2 == 0 if j % 2==0 ]

print(even)
"""

"""
for i in a:
    for j in b:
        if i % 2 == 0 and j % 2 == 0:
            even.append((i,j))

"""

#  Dictionay Comprehension :

"""

syntax :

    {key_expression : value_expression for item in iterable if condition}

"""

# Example :

"""
numbers = [1,2,3,4,5]


# square = {i : i**2 for i in numbers}
# print(square)

even_square = {i : i**2 for i in numbers if i % 2 == 0}

print(even_square)

"""


# Set Comprehension :

"""
Syntax :

    {expression for item in iterable if condition}

"""

# Example :

"""
numbers = {1,2,2,3,4,4,5,6,7,8,8}

squares = {i**2 for i in numbers}

print(squares)

"""

# Real world example :

data = ["Deepika@gamil.com","Hari","John@gmail.com","Guru","Apple","Mathan@yahoo.com","varun@email.com"] 

emails = [i for i in data if "@" in i]

print("\n",emails)