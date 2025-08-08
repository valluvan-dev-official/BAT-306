# Data Types :

"""
Numeric DataType :

    integer :

        integer is Whole Number.
        Positive Or Negative
        Without Decimals
        Unlimited Length

    float :

        Floating Point Numbers
        Positive Or Negative
        With Decimals
        Unlimited Length
        e - Scientific Numbers - Like power 10

    Complex :

        'j' as imaginary number

        Complex Data type used for Scientific Application, Mathematical Based Applications and Electrical and Electronic Based Applications 

        c , c++ ,java not Having this Data type only python have it

        x = real + imaginary

example for Complex :

x = 4 + 5j

print(x.real)
print(x.imag)

"""


#  Text Data Type :

"""
String : str()



comments = ''' welcome to Every One
    Good Morning...
    Good Afternoon...
    Good Evening...
'''

name = "Varun WElcome"
address = 'Chennai'

print(name)
print(address)
print(comments)

"""

# length : len()

# String are Arrays :

"""
name = 'Hello World'

print(name[-11])

# print(len(name))

"""

# Check a String :

"""
name = "Welcome to All"

print("All" in name)

"""


# String Modification :

"""
lower
upper
strip
replace
split

"""

a = "Hello World"

# Lower : Lowercase

# print(a.lower())

# Upper : UpperCase 

# print(a.upper())


#  Strip :

"""
    Remove Whitespace

example :

print(a)

print(a.strip())

"""


# Replace : replace(old,new,count)

# a = "Hello World welocme World to World "

# print(a.replace("World","Avengers",2))


# Split() :

# print(a.split("o"))



# ============= String Concatenation ===========

"""
    We cannot combine strings and Numbers
    But we can combine strings with strings

example:


a = "Hello"

b = "45"

c = a + " " + b

print(c)

"""

# Format strings : format()

"""
    The Format method takes Unlimited Number of Arguments
    are placed into the respective placeholders - {}
"""

# names = "Varun"

# office = "Google"

# salary = 60000



# msg = "hi i'm {2} - i'm working in {0} and my salary is {1}" 

# print(msg.format(office,salary,name))


# F-Strings :




# msg = f"Hi i'm {name} i'm working in {office} and my Salary is {salary}"

# print(msg)


# ======= String Slicing =======

# a[start : end (n-1): step]

# Positive index

# a = "H e l l o   w o r l d"
##     0 1 2 3 4 5 6 7 8 9 10


# Negative index : (n-1) = (-7-1)
"""
   -11 -10 -9 -8 -7  -6 -5  -4 -3 -2 -1
a = h   e   l  l  o      w   o  r  l  d

"""

"""
a = "hello world"

# print(a[3:11])


print(a[0:8:3])

"""

# Escape Character :

"""
- \'
- \\
- \"
- \b
- \f
- \n
- \r
- \t
- \v



name = "hi varun \nWelcome"

print(name)

"""

# ============ Collections ============

# Sequence Data Type :

"""
List
Tuple
Range

"""

# 1. List :

"""
fruits = ['Apple',"Orange","Mango","Banana","Apple"]

    - Lists are used to Store Multiple items in a single variable
    
    - Lists are ordered, changeable and allow duplicate values
    Changeable Means :

        we can change,add,remove items in a list after it has been created
    
    - list items it can be any datatype

    a = [3.4,5,True,"Hello",[1,2,3,4]]

Example

a = [3.4,5,True,"Hello",[1,2,3,4]]

print(a)
print(type(a))

"""

#  List Constructor : list()

"""
a = list("1")
print(a)

"""

# Access List :

"""
    Using index to print the values
    using Positive and negative index slicing


#          -6       -5       -4      -3       -2      -1

fruits = ["Apple","Orange","Mango",'Banana',"Cherry","Grapes"]

#           0        1        2       3        4        5

 print(fruits[2])

# fruits[4] = "Pineapple"

# print(fruits[-3])


# list Slicing : [start : end (n-1) : step ]

# sliced_List = fruits[-6::5]

# print(sliced_List)

"""

# Change List Items :

"""
#          -6       -5       -4      -3       -2      -1

fruits = ["Apple","Orange","Mango",'Banana',"Cherry","Grapes"]

#           0        1        2       3        4        5


fruits[-5 : -2] = 'red','green','blue','white'

print(fruits)

"""


# Add List Items :

# fruits = ["Apple","Orange","Mango"]

# append :

"""
fruits.append(["Banana","Cherry"])

fruits.append(["Banana","Cherry"])

"""

# Extend :

"""
numbers = [10,20,30,40]

numbers.extend(("varun",))

"""

# Insert Items :

# insert(index, item)

"""
fruits = ["Apple","Orange","Mango"]

fruits.insert(5,"Varun")

print(fruits)

"""

# Remove List Items :

# Remove() :

"""
    More than one item with specified value remove() method removes the first occurrence
"""

fruits = ["Apple","Orange","Mango",'Apple']

# print(fruits.remove("Apple"))


# Pop() :

"""
    Removed the Specified index
    default remove the last index
"""

# fruits.pop()


# Del Keyword :

# del fruits[0 : 2]


# Clear() :

"""
    Clears the list

fruits.clear()

fruits.append((1,2,3,4))

print(fruits)

"""


# List Sort() :

"""
    This will sort the list alphanumerically ascending and descending order
    by defult ascending

    sort() case sensitive resulting in all capital letters being sorted before lower case letters
"""

"""
numbers = [100,23,45,10,67,53,97,83,12]

numbers.sort()

numbers.sort(reverse=True)

--------------

fruits = ["Apple" ,"Orange","Cherry","Mango","Banana","banana",'mango','cherry','apple','papaya']

fruits.sort()

fruits.sort(reverse=True)

print(fruits)

"""

# Reverse :

"""
fruits = ['Apple',"Orange","Cherry","Mango"]

fruits.reverse()

print(fruits)

"""

# --------- Task --------

"""
get input from user

x = 10 20 30 40

output should be an list
"""


# Copy a List : copy()

"""
number = [10,20,30,40]

# x = list(number)

x = number.copy()

print(x)

"""

# Join a List :

"""
a = [1,2,3,4]

b = [5,6,7,8]

z = a + b 

print(z)

"""


# ========= Tuple ==========

"""
    (10,30,40)

    Used to Store multiple items in a single variable
    Ordered and Unchangeable
    allow duplicates


    tuple()

# Example : 

fruits = ("Apple","Orange","Mango")

print(fruits)

print(type(fruits))

"""

# Constructor :

"""
x = tuple((10,))

print(x)

"""

# Update a Tuple :

# fruits = ("Apple","Orange","Mango")

# convert to list :

"""
x = list(fruits)

x.append("varun")

fruits = tuple(x)

fruits[0] = "banana"

print(fruits)

"""

# unpack a tuple : # Using Asterik :

"""
fruits = ("Apple","Orange","Mango","cherry")

*a,b,c = fruits 

print(a,b,c)

"""

# Remove Tuple :

"""
fruits = ("Apple","Orange","Mango","cherry")

fruits.remove("Apple")

print(fruits)

"""

# ========== Set ==========

"""
myset = {1,200,"Good",345.67,True}

    Used to strore Multiple items in a single variable
    
    Unordered
    
    do not have a defined order
    
    once set is created, you cannot change its items but you can remove and add new items

    Duplicates Not Allowed

    True and 1 are considered the same value and are treated as a duplicates.

    False and 0 are considered the same value and are treated as a duplicates.

example

myset = {10,"Varun",True,"Appel",1,"Appel"}

print(myset)

"""

# Access Set Items :

"""
Cannot access set items reffering index or key

"""

# fruits = {"apple",'orange','mango','banana'}


# for i in fruits:
#     print(i)


# Add :

# fruits.add(("cerry"))


# Update :

"""
numbers = [1,2,3,4,5]

fruits.update(numbers)

"""

# Join a sets: union()


"""
numbers = {10,20,30,4}

z = fruits.union(numbers)

print(z)

"""

# Common and uncommon datas

"""
fruits = {"apple",'orange','mango','banana'}

veges = {"apple",'Potato','banana','tomato'}

# Intersection :


# a = fruits.intersection(veges)

# fruits.intersection_update(veges)


# Symmetric Difference :

# a = fruits.symmetric_difference(veges)

fruits.symmetric_difference_update(veges)

print(fruits)

# print(a)

"""

# Dictionary :

"""
    dict = {
       "name" : "Varun",
        "age" : 24,
        "city" : "Bangalore",
        "country" : ["India",'USA',"UAE"]
    }

    
    - Data values in key = value pair
    - Ordered
    - Changeable
    - Do Not allowed Duplicates
"""

"""
dict = {
       "name" : "Varun",
        "age" : 24,
        "city" : "Bangalore",
        "country" : ["India",'USA',"UAE"]
}

print(dict)

"""

# Constructor : dict()

"""
a = dict(name = "John",age=35)

print(a)

"""
# Access Dict Items : Using Key
dict = {
       "name" : "Varun",
        "age" : 24,
        "city" : "Bangalore",
        "country" : ["India",'USA',"UAE"],
        "age" :35
}


# print(dict['country'][1])

# dict['nnew'] = "Valluvan"

# Duplicate values :

# Access Items  Using get :

"""
x = dict.get('country')

print(x)

"""

# Get Keys : keys()
"""
    - all the keys from the dict
    if any changes in the ditionary it will replaced in the keys

"""

# print(dict.keys())

# Get Values() :

# print(dict.values())


# Get all items fro the dict :

# print(dict.items())


# Update a Dictionary :

# dict.update({"Year" : 2024,"name" : 'Vimal'})

# print(dict)


# Remove Dictionary Items :

"""
pop()
popitem()
del
clear()
"""
# pop () :

# print(dict.pop("age"))

# popitem() :

# print(dict.popitem())

# del :

# del dict

# print() 

# Copy a dict : copy(),dict()


# Nested Dictionary :

"""
fam = {
    "child1" : {"name" : "Rohan", "age" : 10},
    "child2" : {"name" : "Rahul", "age" : 20},
    "child3" : {"name" : {"Ravi":{"office" : "ZOHO", "Salary" : 50000}}, "age" : 15}
}

# print(fam)
print(fam["child3"]['name']['Ravi']["Salary"])

"""

# child1 = {"name" : "Rohan", "age" : 10}

# child2 = {"name" : "Rahul", "age" : 20},

# fam = {
#     "child1" : child1,
#     "child2" : child2,
#     "child4" : child1
# }

# print(fam)

# =============================

fruits = {"apple",'orange','mango','banana'}

veges = {"apple",'Potato','banana','tomato'}

# Intersection :


# a = fruits.intersection(veges)

# fruits.intersection_update(veges)

a = fruits.symmetric_difference(veges)

fruits.symmetric_difference_update(veges)

print(fruits)
# print(a)