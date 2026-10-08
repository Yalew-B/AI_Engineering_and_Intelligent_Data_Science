# Data Structures in Python
# A data structure is a way of organizing and storing data in a computer so that it can be accessed and modified efficiently.
# Common data structures in Python include lists, tuples, sets, and dictionaries.
#1. Lists in Python
# A list is an ordered collection of elements that can be of different types.
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Adding elements to a list
my_list.append(6)   
print(my_list)

# Removing elements from a list
my_list.remove(1)
print(my_list)

# Accessing elements in a list
print(my_list[0])  # Output: 2
print(my_list[-1])  # Output: 6

#2. Tuples in Python
# A tuple is an ordered collection of elements that cannot be changed (immutable).  
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5

#3. Sets in Python
# A set is an unordered collection of unique elements.
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Adding elements to a set
my_set.add(6)
print(my_set)

# Removing elements from a set
my_set.remove(1)
print(my_set)

#4. Dictionaries in Python
# A dictionary is an unordered collection of key-value pairs.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict)

# Adding elements to a dictionary
my_dict['country'] = 'USA'
print(my_dict)

# Removing elements from a dictionary
del my_dict['age']
print(my_dict)

# Accessing elements in a dictionary
print(my_dict['name'])  # Output: Alice 
print(my_dict['age'])   # Output: 25
print(my_dict['city'])  # Output: New York
print(my_dict['country'])  # Output: USA

#5. Conclusion
# In this code, we have demonstrated the basic usage of common data structures in Python, including lists, tuples, sets, and dictionaries. Each data structure has its own characteristics and use cases, and understanding them is essential for efficient programming in Python.  

#good luck with your learning journey in Python data structures!

#git commit -m "Added Data_Structure.py with examples of lists, tuples, sets, and dictionaries"
