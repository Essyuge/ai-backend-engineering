# 1. Regular methods
# Regular methods are the most common type of method in Python classes.
# They are defined using the `def` keyword and take `self` as the first parameter, which refers to the instance of the class.
# Regular methods can access and modify the instance's attributes and can perform any operations that are needed to manipulate the data of the instance.
# Here is an example of a regular method in a class:
class Employee:
    def __init__(self, first,last, age, position):
        self.first = first
        self.last = last
        self.age = age
        self.position = position

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def display_info(self):
        print(f"Name: {self.fullname()}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")

employee1 = Employee("John", "Doe", 30, "Software Engineer")
employee1.display_info()  # This will call the display_info method and print the employee's information

# 2. Class methods
# Class methods are defined using the `@classmethod` decorator and take `cls` as the first parameter, which refers to the class itself rather than an instance of the class.
# Class methods can be used to create factory methods that return an instance of the class, 
# or to perform operations that are related to the class rather than a specific instance.
class Employee:
    company_name = "Tech Company"  # This is a class variable

    def __init__(self, first,last, age, position):
        self.first = first
        self.last = last
        self.age = age
        self.position = position

    @classmethod
    def from_string(cls, employee_str):
        first, last, age, position = employee_str.split(',')
        return cls(first, last, int(age), position)
employee_str = "John,Doe,30,Software Engineer"
employee1 = Employee.from_string(employee_str)  # This will create an instance of Employee using the from_string class method
employee1.display_info()  # This will call the display_info method and print the employee's information

# 3. Static methods
# Static methods are defined using the `@staticmethod` decorator and do not take `self` or `cls` as the first parameter. 
# They are used to define methods that are related to the class but do not require access to the instance or class attributes. 
# Static methods can be called on the class itself or on an instance of the class.
class Employee:
    company_name = "Tech Company"  # This is a class variable

    def __init__(self, first,last, age, position):
        self.first = first
        self.last = last
        self.age = age
        self.position = position

    @staticmethod
    def is_adult(age):
        return age >= 18

employee1 = Employee("John", "Doe", 30, "Software Engineer")
print(Employee.is_adult(20))  # This will print True
print(employee1.is_adult(16))  # This will print False