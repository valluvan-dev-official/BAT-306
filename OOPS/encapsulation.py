# Public Method 

"""
class Person:

    name = "Varun"

    mail = "varun@example.com"

    def Office(self):

        print("My salary is 60000")
        print("I work in a software company")
        print("My Domain Password is AV@2345")


    def myfun(self):

        print("This is a public method")



obj = Person()

print(obj.name)

print(obj.mail)

obj.Office()

obj.myfun()

"""

# Private Method

"""
class Person:

    name = "Varun"

    __mail = "varun@example.com"

    def __Office(self):

        print("My salary is 60000")
        print("I work in a software company")
        print("My Domain Password is AV@2345")


    def myfun(self):

        print("This is a public method")
        print("My email is", self.__mail)
        print("My office details are:")
        self.__Office()


# obj = Person()

# print(obj.name)

# print(obj.__mail)

# obj.Office()

# obj.myfun()


class Sub_person(Person):

    def mySub_fun(self):

        print("This is a public method in the subclass")
        print(self.__mail)
       


obj = Sub_person()

obj.mySub_fun()

"""

# Protected


class Person:

    name = "Varun"

    _mail = "varun@example.com"

    def _Office(self):

        print("My salary is 60000")
        print("I work in a software company")
        print("My Domain Password is AV@2345")


    def myfun(self):

        print("This is a public method")
        print("My email is", self._mail)
        print("My office details are:")
        self._Office()

"""
obj = Person()

print(obj.name)
print(obj.mail)

obj.Office()

# obj.myfun()

"""

class Employee(Person):

    def new_fun(self):

        print("This is a public method in the subclass")
        print("My email is", self._mail)
        print("My office details are:")
        self._Office()





obj = Employee()

print(obj.name)

print(obj._mail)

obj._Office()