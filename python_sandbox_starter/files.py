# Python has functions for 
# creating,
#  reading,
#  updating, 
# and deleting files.
# Open a file for writing (this will create the file if it doesn't exist)


myfile = open('myfile.txt', 'w')  # This will create a new file called myfile.txt in the current directory
# print(myfile)  # <_io.TextIOWrapper name='myfile.txt' mode='w' encoding='UTF-8'> (file object)
# print(type(myfile))  # <class '_io.TextIOWrapper'> (type of the file object)
print(myfile.name)  # myfile.txt (name of the file)
print(myfile.mode)  # w (mode in which the file is opened)
print(myfile.closed)  # False (whether the file is closed or not)

# Write some text to the file
myfile.write('Hello, this is a file created in Python.\n')
myfile.write('This file is used to demonstrate file handling in Python.\n')
myfile.write('Python makes it easy to work with files.\n')


# Close the file
myfile.close()
print(myfile.closed)  # True (whether the file is closed or not)
# myfile.write('This will raise an error because the file is closed.')  # This will raise an error because the file is closed
myfile=open('myfile.txt', 'r')  # Open the file for reading
content = myfile.read()  # Read the entire content of the file
print(content)  # Hello, this is a file created in Python. This file is used to demonstrate file handling in Python. Python makes it easy to work with files. (the content of the file)
myfile.close()  # Close the file after reading

myfile = open('myfile.txt', 'a')  # Open the file for appending (this will add to the end of the file instead of overwriting it)
myfile.write('This line is added to the end of the file.\n')  # This will add a new line to the end of the file
myfile.close()  # Close the file after appending