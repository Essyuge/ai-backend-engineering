# A dictionary is a built-in data structure that stores data as key–value pairs.
# A Dictionary is a collection which is unordered,
#  changeable and indexed.
#  No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
person = {'name': 'john', 'age': 30, 'is_cool': True}
print(type(person))  # <class 'dict'>
print(person)  # {'name': 'john', 'age': 30, 'is_cool': True}
print(person['name'])  # john (accessing value by key)
print(person.get('age'))  # 30 (accessing value by key using get method)
print(person.get('address', 'Not Found'))  # Not Found (returns default value if key is not found)
person['name'] = 'jane'  # Updating value by key    
print(person)  # {'name': 'jane', 'age': 30, 'is_cool': True}
person['address'] = '123 Main St'  # Adding a new key-value pair
print(person)  # {'name': 'jane', 'age': 30, 'is_cool': True, 'address': '123 Main St'}
print(person.keys())  # dict_keys(['name', 'age', 'is_cool', 'address']) (returns a view of the keys)
print(person.values())  # dict_values(['jane', 30, True, '123 Main St']) (returns a view of the values)
print(person.items())  # dict_items([('name', 'jane'), ('age', 30), ('is_cool', True), ('address', '123 Main St')]) (returns a view of the key-value pairs)
person.pop('age')  # Removes the key 'age' and returns its value
print(person)  # {'name': 'jane', 'is_cool': True, 'address': '123 Main St'}
person.popitem()  # Removes and returns the last key-value pair as a tuple
print(person)  # {'name': 'jane', 'is_cool': True} (order may vary)
person.clear()  # Removes all items from the dictionary

# use constructors to make a dictionary
person2 = dict(name='john', age=30, is_cool=True)
print(person2)  # {'name': 'john', 'age': 30, 'is_cool': True}
person3 = dict([('name', 'john'), ('age', 30), ('is_cool', True)])
print(person3)  # {'name': 'john', 'age': 30, 'is_cool': True}
person4 = dict(zip(['name', 'age', 'is_cool'], ['john', 30, True]))
print(person4)  # {'name': 'john', 'age': 30, 'is_cool': True}  
person5 = person2.copy()  # Creates a shallow copy of the dictionary
print(person5)  # {'name': 'john', 'age': 30, 'is_cool': True}
del person5['age']  # Deletes the key 'age' from the dictionary
print(person5)  # {'name': 'john', 'is_cool': True}


# list of dictionaries
people = [
    {'name': 'john', 'age': 30, 'is_cool': True},   
    {'name': 'jane', 'age': 25, 'is_cool': False},
    {'name': 'bob', 'age': 35, 'is_cool': True} 
]
print(people)  # [{'name': 'john', 'age': 30, 'is_cool': True}, {'name': 'jane', 'age': 25, 'is_cool': False}, {'name': 'bob', 'age': 35, 'is_cool': True}]
print(people[0])  # {'name': 'john', 'age': 30, 'is_cool': True} (accessing the first dictionary in the list)
print(people[0]['name'])  # john (accessing the value of 'name' in the first dictionary)    
