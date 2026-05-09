# If/ Else conditions are used to decide to do something based on something being true or false
X = 10
if X > 5:
    print('X is greater than 5')
else:
    print('X is not greater than 5')

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
X = 10
if X > 5:
    print('X is greater than 5')    
else:
    print('X is not greater than 5')

# Logical operators (and, or, not) - Used to combine conditional statements
X = 10
if X > 5 and X < 15:
    print('X is greater than 5 and less than 15')
else:
    print('X is not greater than 5 and less than 15')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
X = 10
numbers = [1, 2, 3, 4, 5]
if X in numbers:
    print('X is in the list')
else:
    print('X is not in the list')

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
X = 10
Y = 10
if X is Y:
    print('X and Y are the same object')
else:
    print('X and Y are not the same object')