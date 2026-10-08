# Lists in Python
# A list is a collection of items that are ordered and changeable.
# Lists are written with square brackets.
my_list: list[int] = [1, 2, 3, 4, 5]
print(my_list)

# Accessing elements in a list
#Accessing elements in a list is done using indexing.
# The first element has an index of 0, the second element has an index of 1, and so on.
# Negative indexing starts from the end of the list, with -1 being the last element.
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

# Modifying elements in a list
# Lists are mutable, meaning you can change their content.
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Adding elements to a list
# You can add elements to a list using the append() method, which adds an element to the end of the list.
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements from a list
my_list.remove(10)
print(my_list)  # Output: [2, 3, 4, 5, 6]

# Slicing a list
print(my_list[1:4])  # Output: [2, 3, 4]
#indicing a list
print(my_list[::2])  # Output: [2, 4, 6]

# Length of a list
print(len(my_list))  # Output: 5

# Iterating through a list
for item in my_list:
    print(item)

# List comprehension
squared_list = [x**2 for x in my_list]
print(squared_list)  # Output: [4, 9, 16, 25, 36]

# Sorting a list
my_list.sort()
print(my_list)  # Output: [2, 3, 4, 5, 6]

# Copying a list
copied_list = my_list.copy()
print(copied_list)  # Output: [2, 3, 4, 5, 6]

# Clearing a list
my_list.clear() 
print(my_list)  # Output: []

# git commit -m "Added list.py with examples of list operations in Python"