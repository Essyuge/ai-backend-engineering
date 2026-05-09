# A List is a collection which is ordered and changeable. Allows duplicate members.
# Lists are written with square brackets.
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
# Get a value from a list
print(fruits[0])  # apple
print(fruits[1])  # banana
print(numbers[1])  # 2

# Use constructors to make a list
numbers2 = list((1, 2, 3, 4, 5))
print(numbers2)  # [1, 2, 3, 4, 5]
print(type(numbers2))  # <class 'list'>
print(len(numbers2))  # 5
print(fruits[-1])  # orange (last item)
print(fruits[0:2])  # ['apple', 'banana'] (slicing)
print(fruits[:2])  # ['apple', 'banana'] (slicing from the beginning)
print(fruits[1:])  # ['banana', 'orange'] (slicing to the end)
print(fruits[-2:])  # ['banana', 'orange'] (slicing the last two items)
print(fruits + ['grape', 'kiwi'])  # ['apple', 'banana', 'orange', 'grape', 'kiwi'] (concatenation)
print(fruits * 2)  # ['apple', 'banana', 'orange', 'apple', 'banana', 'orange'] (repetition)
fruits.append('grape')  # Adds 'grape' to the end of the list
print(fruits)  # ['apple', 'banana', 'orange', 'grape']
print(fruits.index('banana'))  # 1 (index of the first occurrence of 'banana')
print(fruits.count('apple'))  # 1 (number of occurrences of 'apple')
fruits.sort()  # Sorts the list in place
print(fruits)  # ['apple', 'banana', 'grape', 'orange']
fruits.reverse()  # Reverses the list in place
print(fruits)  # ['orange', 'grape', 'banana', 'apple']
fruits.insert(1, 'kiwi')  # Inserts 'kiwi' at index 1
print(fruits)  # ['orange', 'kiwi', 'grape', 'banana', 'apple']
fruits.remove('banana')  # Removes the first occurrence of 'banana'
print(fruits)  # ['orange', 'kiwi', 'grape', 'apple']
fruits.pop()  # Removes and returns the last item
fruits.append('banana')  # Adds 'banana' to the end of the list
print(fruits)  # ['orange', 'kiwi', 'grape', 'apple', 'banana']

print(fruits)  # ['orange', 'kiwi', 'grape']
fruits.pop(0)  # Removes and returns the item at index 0
print(fruits)  # ['kiwi', 'grape']
fruits.clear()  # Removes all items from the list
print(fruits)  # []
