# Loops in Python :

"""
    Loops in Python Allow you to execute a block of code multiple times.
    python Supports two main types of loops :

            1. For Loop
            2. While Loop


1. For Loop :

    a for loop is a control flow  statement in programming that allows you to execute ablock of code repeatedly for a specific number of times
    It's Particularly useful when you know in advance how may times you want to execute a certain block of code.

    Key Features :

        Used to iterate over a sequence like a list, tuple, dictionary, set, or string.
        Executes a set of statements for each item in the sequence.
        Iteration is finite and predefined by the length of the sequence.

    Syntax :    

        for variable in iterables:
            # code to be executed

"""


# fruits = ["Apple","Orange","Mango","Banana"]


# for i in fruits: 

#     print(i)


"""
numbers = [10,15,20,35,40]

even = []

odd = []

for i in numbers:

    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i*5)


print("Even - numbers :- ", even)

print("Odd - numbers :- ", odd)

"""

# Break and Continue:

"""
break: Exits the loop prematurely.

continue: Skips the current iteration and moves to the next one.

"""

# Example:

"""
fruits = {"Apple","Orange","Mango","Papaya"}

for i in fruits:

    if i == "Mango":
        break
        # continue

    print(i)

"""

# Else in For Loop :

"""
    The ELse Block in a for loop executes if the loop completes without encountering a break statement.

"""
# Example :

"""
fruits = ["Apple","Orange","Mango","Papaya"]

for i in fruits:

    if i == "Papaya":
        # break
        continue

    print(i)
else:
    print("Loop Finished")

"""
# Nested Loops :

"""
- A loop inside another loop is called a nested loop.
- The inner loop will run for each iteration of the outer loop.
- inner loop will be executed onetime for each iteration of the outer loop.

"""

# Example :
"""
fruits = ["Apple","Orange","Mango","Papaya"]

childrens = ["Amar","Varun","Hari","Rooban"]


for i in fruits: # apple

    for j in childrens: # Amar varun hari rooban

        print(i," - ",j) #[apple,amar] [apple,varun] [apple,hari] [apple,rooban]

"""

# Range Function:

# range(start,stop(n-1),step)

"""
- range() is a built-in function in python.
- range() is used to generate a sequence of numbers.
- range() is used to iterate over a sequence of numbers.
- range() is used to generate a sequence of numbers from 0 to n-1.

Generates a sequence of numbers, commonly used in for loops.

"""

"""
for i in range(1,10,3):
    
    print(i)

"""

# 2.  While Loop :

"""
- while loop is used to execute a block of code repeatedly.
- while loop is used to execute a block of code repeatedly until a certain condition is met.
- can execute a set of statements as long as a condition is true 

while something_is_true:
    do something repeatedly

Key Features:

Executes a block of code as long as a specified condition is True.
The number of iterations depends on the condition.

syntax :

while condition:
    # Code to execute while the condition is True

"""


"""
x = 0 # 1 2 3 4 5

while x < 5: # 0 1 2 3 4 5

    x += 1 

    print(x) # 0 1 2 3 4

    # x += 1 # 1 2 3 4 


"""

"""
countdown = 5

while countdown > 0:

    print(countdown) # 5 4 3 2 1

    countdown -= 1

"""

# Break and Continue in While Loops

"""
i = 0

while i < 5:
    
    i += 1

    if i == 3:
        # break
        continue
    
    print(i) # 0 1 2 
    
"""

# Use Else in While Loop :

i = 0 

while i < 6:

    i += 1
    
    if i == 3 :
        continue

    print(i) 

    # i += 1
else:
    print("Loop completed without break")
