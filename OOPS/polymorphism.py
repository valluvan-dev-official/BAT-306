# Method Overloading:


"""
class Calcculator:

    def add(self,a):

        print("Adding:", a)

    def add(self,a,b):

        print("Adding:", a + b)

    def add(self,a,b,c):

        print("Adding:", a + b + c)


obj = Calcculator()

# obj.add(5)

# obj.add(5, 10)

obj.add(5, 10, 15)

"""

# Proper Method Overloading :


class Calculator:

    def add(self,a = 0,b = 0,c = 0):

        print("Adding:", a + b + c)



obj = Calculator()

obj.add(5)

obj.add(5, 10)

obj.add(5, 10, 15)
