# Python object oriented programming (OOP) is a programming paradigm that uses objects and classes to structure code.
#  It allows for the creation of reusable and modular code, making it easier to manage and maintain.
# A class is a blueprint for creating objects, and an object is an instance of a class. 
# Classes can have attributes (data) and methods (functions) that operate on the data.
# In Python, you can define a class using the `class` keyword, followed by the class name and a colon.
# Here is an example of a simple class definition for an Employee:
class Employee:
    def __init__(self, first,last, age, position):
        self.first = first
        self.last = last
        self.age = age
        self.position = position

    def fullname(self):
        return f'{self.first} {self.last}'
    
    # def display_info(self):
    #     print(f"Name: {self.name}")
    #     print(f"Age: {self.age}")
    #     print(f"Position: {self.position}")

# In this example, the `Employee` class has an `__init__` method, which is a special method that is called when an object is created.
# It initializes the attributes of the class with the values passed as arguments.
# The `display_info` method is a regular method that prints the employee's information.
# To create an instance of the `Employee` class, you can do the following:
employee1 = Employee("John", "Doe", 30, "Software Engineer")
# employee1.display_info()
# print(f"Name: {employee1.fullname()}")
# print(f"Age: {employee1.age}")
# print(f"Position: {employee1.position}")
# print(employee1.__dict__)  # This will print the attributes of the employee1 object as a dictionary
# print(employee1) 
print(employee1.fullname())

# class variables are shared among all instances of the class, 
# while instance variables are unique to each instance.
# In the example above, `first`, `last`, `age`, and `position` are instance variables,
#  as they are defined within the `__init__` method and are unique to each instance of the `Employee` class.
#  If we were to define a class variable, it would be defined outside of any method and would be shared among all instances of the class. 
# For example:    
class Employee:
    company_name = "Tech Company"  # This is a class variable

    def __init__(self, first,last, age, position):
        self.first = first
        self.last = last
        self.age = age
        self.position = position

    def fullname(self):
        return f'{self.first} {self.last}'
    
employee1 = Employee("John", "Doe", 30, "Software Engineer")
employee2 = Employee("Jane", "Smith", 28, "Data Scientist")

print(employee1.company_name)  # Output: Tech Company
print(employee2.company_name)  # Output: Tech Company


