# A for loop is used for iterating over a sequence
#  (that is either a list,
#  a tuple,
#  a dictionary,
#  a set,
#  or a string).
people = ['John', 'Jane', 'Doe']
for person in people:
    print(person)  # John, Jane, Doe (each name on a new line)

# Breaking out of a loop
for person in people:
    if person == 'Jane':
        break  # This will stop the loop when it reaches 'Jane'
    print(person)  # John (only John will be printed)

    # continuing to the next iteration
    for person in people:
        if person == 'Jane':
            continue  # This will skip the rest of the loop when it reaches 'Jane' and continue with the next iteration
        print(person)  # John, Doe (Jane is skipped)

# Range function - The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4 (each number on a new line)

for i in range(len(people)):
    print(people[i])  # John, Jane, Doe (each name on a new line)

for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9 (each number on a new line)

for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (each number on a new line)

for i in range(5):
    for j in range(3):
        print(f'i: {i}, j: {j}')  # Nested loop example (prints the values of i and j)

# While loops execute a set of statements as long as a condition is true.
count = 0
while count<= 10:
    print(f'count: {count}')  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (each number on a new line)
    count += 1

while True:
    response = input('Enter a number (or "exit" to quit): ')
    if response.lower() == 'exit' or response.lower() == 'quit':
        break  # This will exit the loop if the user types 'exit' or 'quit'
    try:
        number = int(response)
        print(f'You entered: {number}')  # This will print the number entered by the user
    except ValueError:
        print('Please enter a valid number or "exit" to quit.')  # This will handle the case where the user enters something that is not a number