# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = "John"
age = 30

# concatenation
# print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old')

# Argumanented string formatting
print('Hello, my name is {} and I am {} years old'.format(name, age))

# String Formatting
# Old style
print("Hello, my name is %s and I am %d" % (name, age))
# New style
print("Hello, my name is {} and I am {}".format(name, age))
# f-strings (Python 3.6+)
print(f"Hello, my name is {name} and I am {age}")

# # String Methods
s = "hello world"
print(s.upper())  # HELLO WORLD
print(s.lower())  # hello world
print(s.title())  # Hello World
print(s.strip())  # hello world (removes leading/trailing whitespace)
print(s.split())  # ['hello', 'world']
print(s.replace("world", "there"))  # hello there
print("hello" in s)  # True
print(s.find("world"))  # 6 (index of the first occurrence of "world")
print(s.count("o"))  # 2 (number of occurrences of "o")
print(s.startswith("hello"))  # True
print(s.endswith("world"))  # True
print(s.isalpha())  # False (contains space)
print(s.isdigit())  # False (not all characters are digits)
print(s.islower())  # True (all characters are lowercase)
print(s.isupper())  # False (not all characters are uppercase)
print(s.isalnum())  # False (contains space)
print(s.center(20, "*"))  # *****hello world***** (centers the string with padding)
print(s.ljust(20, "*"))  # hello world********** (left-justifies the string with padding)
print(s.rjust(20, "*"))  # **********hello world (right-justifies the string with padding)
print(len(s))  # 11 (length of the string)
print(s[0])  # h (first character)
print(s[-1])  # d (last character)
print(s[0:5])  # hello (substring from index 0 to 4)
print(s[6:])  # world (substring from index 6 to the end)
print(s[:5])  # hello (substring from the beginning to index 4)