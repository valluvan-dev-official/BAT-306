# Open a file :
"""
Syntax :

    open(filename,mode)
"""

"""
close files :
    a good practice to always close the file when you are done with it.

"""
# f = open("sam.txt")

# print(f.read(10))
# print(f.read())


# print(f.readline())
# print(f.readline())


# print(f.readlines())

# print(f.read(10))

# f.close()


# print(f.read())


# Writing File :

# Write Mode :


"""
f = open("new_text_file.txt",'w')

f.write("Hello, this is a new file.")

f.close()

"""


# Append Mode :

"""
f = open("new_text_file.txt",'a')

f.write("\nHello, this is an appended line.")

f.close()

"""

# Create Mode :

"""
f = open("sample1.txt", 'x')

f.write("Hello, this is a new file.")

f.close()
"""


# Delete a File :

"""
import os 


# os.remove("sample1.txt")

# Check if the file is exists or not :

'''
if os.path.exists("sample1.txt"):
    print("File exists")
    os.remove("sample1.txt")
else:
    print("File does not exist")
    
'''

# Remove a Folder :

# Empty folder


os.rmdir("empty")

"""


# File Handling Methods :

f = open("sam.txt", 'r')


# print(f.mode)

# print(f.readable())

# print(f.writable())


# Tell :

"""
print(f.tell())

print(f.read(10))

print(f.tell())

"""

# Seek :

"""
f.seek(10)

print(f.read(10))

print(f.tell())

"""


# Context Manager :

"""
with open("sam.txt",'r') as f:
    print(f.read(10))

print(f.read(10))

"""

# Writing Multiple Lines to a file :

"""
lines = ["Hello, this is line 1.", "\nHello, this is line 2.", "\nHello, this is line 3."]

with open("new_file.txt",'w') as x:

    x.writelines(lines)

"""


# File handling with CSV

import csv

# Creating a csv file

"""
with open("sample.csv", 'w') as csvfile:

    w = csv.writer(csvfile)
    w.writerow(["Roll-No","Name","Marks"])
    w.writerow([1,"John",85])
    w.writerow([2,"Jane",90])
    w.writerow([3,"Doe",78])
"""

# Read a csv File :

"""
with open("sample.csv",'r') as f:

    reader = csv.reader(f)

    # print(r)

    for data in reader:
        
        for i in data:
            print(i)

"""

"""
f = open("sample.csv")

reader = csv.reader(f)

l = list(reader)

# print(l)

for line in l:
    # print(line)

    for data in line:
        # print(data)
        print(data,end = " ")
    print()

"""


from zipfile import *

"""
with ZipFile("demo.zip","w") as z:
    z.write("sample.txt")

"""

# with ZipFile("demo.zip",'r') as z:
#     z.extractall("extracted_files")


"""
f = ZipFile("demo.zip", 'r',ZIP_STORED)

filenames = f.namelist()
# print(filenames)

for filename in filenames:
    if filename == "sample.txt":
        f1 = open("sample.txt")
        print(f1.read())
        f1.close()

"""

# Working with Binary :

"""
f = open("img1.jpeg",'rb')

data = f.read()

# print(data)

f1 = open("Thanos.jpeg","wb")

f1.write(data)
f1.close()

"""


# Exception Handling in File Operation :

try:
    f = open("news1.txt",'x')

    try:

        f.write("Welcome to File Handling")

    except:
        print("Somthing happen when write a file")

    finally:
        f.close()


except Exception as e:

    print("Something happen when open a file",e)