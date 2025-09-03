class Student:

    def __init__(self,name,age):
        self.name = name
        self.__age = age


    def get_age(self):
        return self.__age

    def set_age(self, new_age):

        if new_age > 0:
            self.__age = new_age
            print("Age updated successfully.")

        else:
            print("Invalid age. Age must be positive.")


student1 = Student("Alice", 20)


print(student1.name)  # Accessing public attribute
print(student1.get_age())  # Accessing private attribute via getter


student1.set_age(4)

print(student1.get_age())  # Accessing modified private attribute via getter