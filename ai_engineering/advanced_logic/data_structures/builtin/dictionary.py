# Dictionaries in Python
# A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed.
# Dictionaries are written with curly brackets.
my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}
print(my_dict)

# Accessing elements in a dictionary
# Elements in a dictionary are accessed using their keys.
print(my_dict["a"])  # Output: 1

# Modifying elements in a dictionary
# You can change the value of an existing key or add a new key-value pair.
my_dict["a"] = 10
print(my_dict)  # Output: {"a": 10, "b": 2, "c": 3}

# Adding elements to a dictionary
my_dict["d"] = 4
print(my_dict)  # Output: {"a": 10, "b": 2, "c": 3, "d": 4}

# Removing elements from a dictionary
del my_dict["a"]
print(my_dict)  # Output: {"b": 2, "c": 3, "d": 4}

# Iterating through a dictionary
for key in my_dict:
    print(key, my_dict[key])

# Dictionary methods
print(my_dict.keys())   # Output: dict_keys(['b', 'c', 'd'])
print(my_dict.values()) # Output: dict_values([2, 3, 4])
print(my_dict.items())  # Output: dict_items([('b', 2), ('c', 3), ('d', 4)])

# Copying a dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {"b": 2, "c": 3, "d": 4}

# Clearing a dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Nested dictionaries
# A dictionary can contain another dictionary as a value.
nested_dict: dict[str, dict[str, int]] = {
    "dict1": {"a": 1, "b": 2},
    "dict2": {"c": 3, "d": 4}
}
print(nested_dict)  # Output: {"dict1": {"a": 1, "b": 2}, "dict2": {"c": 3, "d": 4}}

# Accessing elements in a nested dictionary
print(nested_dict["dict1"]["a"])  # Output: 1
print(nested_dict["dict2"]["c"])  # Output: 3

# Dictionary comprehension
# You can create a dictionary using dictionary comprehension.
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

