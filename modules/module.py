"""
import main


print(main.name)
print(main.age)
print(main.add_numbers(5, 10))
main.myfun("Varun")

"""

# import main 

#from main import name,add_numbers 

# from main import * 

# print(name)
# print(add_numbers(5, 10))


from main import name as n,add_numbers as add


print(n)
print(add(5, 10))