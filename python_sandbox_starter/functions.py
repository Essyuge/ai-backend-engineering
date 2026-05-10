# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
# create a function
from unittest import result


def say_hello(name):
    print(f'Hello {name}')

say_hello('John Doe')  # Hello John Doe (calling the function with an argument)
def add_numbers(x, y):
   total = x + y
   return total
num= add_numbers(5, 3)
print(num)  # 8 (the result of the function)

def greet(name, greeting='Hello'):
    print(f'{greeting} {name}')
greet('Alice')  # Hello Alice (using the default greeting)
greet('Bob', 'Hi')  # Hi Bob (overriding the default greeting)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
#  Very similar to JS arrow functions
add = lambda x, y: x + y
print(add(5, 3))  # 8 (the result of the lambda function
greet =  lambda name, greeting = 'Hello':print(f'{greeting} {name}')
greet('Alice')  # Hello Alice (using the default greeting)
greet('Bob', 'Hi')  # Hi Bob (overriding the default greeting

# “Anonymous function” means
# It’s a function without a normal def name.
# You often use it once and immediately.
multiply = lambda a, b: a * b
print(multiply(4, 5))   # 20 (the result of the lambda function)

# Lambda functions are often used with higher-order functions like map(), filter(), and sorted() to perform operations on collections of data.
students = [
    ("John", 80),
    ("Mary", 95),
    ("Alex", 70)
]
students.sort(key = lambda student:student [1])  # Sorts the list of students by their scores (the second item in the tuple)
print(students)  # [('Alex', 70), ('John', 80), ('Mary', 95)] (sorted list of students) 

# mapping a list of numbers to get their squares
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))  # [2, 4, 6, 8] (the result of the map function)

# Filtering a list of numbers to get only the even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6] (the result of the filter function)
