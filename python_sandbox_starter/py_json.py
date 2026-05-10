# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json
# sample JSON string
user ='{"name": "John", "age": 30, "city": "New York"}'
print(type(user))  # <class 'str'> (the JSON data is a string)
print(user)  # {"name": "John", "age": 30, "city": "New York"} (the JSON data as a string)
print(user[5])  # { (accessing the first character of the JSON string)
print(user[1:5])  # "nam (accessing a substring of the JSON string)
# parse x:
user_dict = json.loads(user)
print(user_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}
print(user_dict['name'])  # John (accessing value by key)

# # convert back to JSON
user_json = json.dumps(user_dict)
print(user_json)  # {"name": "John", "age": 30, "city": "New York"}

user_json2 = json.dumps(user_dict, indent=4)  # Pretty print with indentation
print(user_json2)  # {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }