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

f.seek(10)

print(f.read(10))

print(f.tell())
