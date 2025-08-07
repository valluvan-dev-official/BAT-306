# Conditional Satements :

"""
Conditional statements are fundamental in Python for decision-making in programs. They allow the execution of certain blocks of code based on specific conditions. The key conditional statements in Python are if, if-else, if-elif-else, and nested if. These statements use boolean expressions to evaluate whether a condition is True or False.


"""

#  If Statement :

"""
    the if statement executes a block of code only if the condition evaluates to True

    syntax :

        if condition:
            # code block
"""

# example :

"""
age = 14

if age > 12:
    print("You are an adult")

"""

# if - else  statement :

"""
 the if - else statement provides an alternative block of code to execute when the conndition is  false

    Syntax :

        if condition :
            # code block
        else :
            # code block
"""

"""
age = 120

if age > 18 :
    print("You are an adult")
else :
    print("You are a minor")

"""

# if - elif - else :

"""
    the if-elif-else statement allows testing multiple conditions sequentially.
    the first condition evaluates to true
 is executed

    Syntax :

        if condition-1:
            # code block
        elif condition-2:
            # code block
        else :
            # code block

"""

"""
age = int(input("Enter  your age : "))

if age > 18 and age < 60 :
    print("You are an adult")
elif age >= 60 :
    print("You are a senior")
else:
    print("You are a minor")

"""

# Nested if :

"""
    a nested if statement is an if statement inside another if or else block, allowing more complex
    decision making.

    syntax :

        if condition:
            if condition-1:
                # code block
            elif condition-2:
                # code block
            else :
                # code block
        else:
            if condition-1:
                # code block
            else:   
                # code block

"""

"""
x = int(input(" Enter Number : "))

if x > 5:

    if x % 2 == 0:
        print("x is greater than five and is even")
    else:
        print("x is greater than five and is odd")
else:
    if x % 2 == 0:
        print("x is less than or equal to five and is even")
    else:
        print("x is less than or equal to five and is odd")

"""

"""
0 - 12 --> child 
13 - 19 --> Teenager 
20 - 59 --> Adult
60 --> Senior Citizen 

"""