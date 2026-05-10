# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x = 2 #integer
y = 3.5 #float
name =  "john" #str
is_cool = True #bool

# multiple assignments
x, y, name, is_cool = (2, 3.5, "john", True)
print(x, y, name, is_cool)
print(type(x))
print(type(y))
print(type(name))
print(type(is_cool))
print('Hello, my name is ' + name)
print(x,y,name,is_cool)

# type casting
x =str(x) # x is now a string
y = int(y) # y is now an integer