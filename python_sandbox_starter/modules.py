# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, 
# modules you can install using the pip package manager (including Django) as well as custom modules
# core python modules are built into python and can be used without installing anything
import math  # Importing the math module
import datetime  # Importing the datetime module
from datetime import date, time  # Importing the date class from the datetime module
import random  # Importing the random module
print(math.sqrt(16))  # 4.0 (using the sqrt function from the math module)

print(random.randint(1, 10))  # Random integer between 1 and 10


print(date.today() - datetime.timedelta(days=10))  # 10 days ago
print(time())  # Current time in seconds since the epoch
print(datetime.datetime.now())  # Current date and time
print(datetime.date.today())  # Current date

# # pip module example
# import camelcase  # Importing the camelcase module (you need to install it using pip)
# c = camelcase.CamelCase()  # Creating an instance of the CamelCase class
# print(c.hump('hello world'))  # Converting a string to CamelCase

# import custom module example
import validator  # Importing the custom validator module
from validator import validate_email  # Importing the validate_email function from the validator module
print(validate_email('example@example.com'))  # Validating an email address

email = 'example@example.com'
if  validate_email(email):
    print('Valid email')
else:
    print('Invalid email')