# A Tuple is a collection which is ordered and unchangeable.
#  Allows duplicate members.
# tuples are immutable and can not be changed after they are created
#  create a tuple
fruits = ('apple', 'banana', 'orange')
fruits2 = tuple(('apple', 'banana', 'orange'))
print(fruits)  # ('apple', 'banana', 'orange')  
print(fruits2)  # ('apple', 'banana', 'orange')
print(type(fruits))  # <class 'tuple'>
print(len(fruits))  # 3
print(fruits[0])  # apple (first item)
print(fruits[-1])  # orange (last item)
print(fruits2[0:2])  # ('apple', 'banana') (slicing)
# fruits2.append('grape')  # This will raise an error because tuples are immutable
print(fruits2)  # ('apple', 'banana', 'orange') (unchanged)

# A Set is a collection which is unordered and unindexed.
#  No duplicate members.
fruits_set = {'apple', 'banana', 'orange'}
fruits_set2 = set(('apple', 'banana', 'orange'))
print(fruits_set)  # {'apple', 'banana', 'orange'} (order may vary)
print(fruits_set2)  # {'apple', 'banana', 'orange'} (order may vary)
print(type(fruits_set))  # <class 'set'>
print(len(fruits_set))  # 3
# print(fruits_set[0])  # This will raise an error because sets are unordered
print('apple' in fruits_set)  # True (membership test)
fruits_set.add('banana')  # Adds 'banana' to the set note: does not add because 'banana' is already in the set
print(fruits_set)  # {'apple', 'banana', 'orange'} (order may vary)
fruits_set.remove('banana')  # Removes 'banana' from the set note: raises an error if 'banana' is not in the set
print(fruits_set)  # {'apple', 'orange', 'grape'} (order may vary)
fruits_set.discard('banana')  # Removes 'banana' from the set if it exists (no error if it doesn't)
print(fruits_set)  # {'apple', 'orange', 'grape'} (order may vary)
fruits_set.clear()  # Removes all items from the set
print(fruits_set)  # set() (empty set)
