# A class is like a blueprint for creating objects.
#  An object has properties and methods(functions) associated with it.
#  Almost everything in Python is an object
class User:
    # constructor method to initialize the object
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        print(f'Hello, my name is {self.name} and my email is {self.email}')

    def update_email(self, new_email):
        self.email = new_email

      
# initialize an object of the User class
user1 = User('John Doe' , 'john.doe@example.com')
print(user1.name)  # John Doe (accessing the name property of the user1 object)
print(user1.email)  # john.doe@example.com (accessing the email property of the user1 object)

user1.greet()  # Hello, my name is John Doe and my email is john.doe@example.com
user1.update_email('john.new@example.com')
user1.greet()  # Hello, my name is John Doe and my email is john.new@example.com

# Extend the User class to create a new class called Admin that inherits from User
class Admin(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)  # call the constructor of the parent class
        self.role = role

    def admin_greet(self):
        print(f'Hello, I am {self.name} and I am an {self.role}')
admin1 = Admin('Alice', 'alice@example.com', 'Administrator')
admin1.admin_greet()  # Hello, I am Alice and I am an Administrator