# Lists in Python
# A list is a collection of items that are ordered and changeable. 
# Lists are written with square brackets.
# git commit -m "Added lists.py with examples of list operations and comprehensions"
my_list = [1, 2, 3, 4, 5]
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
print(my_list[::2])  # Output: [2, 4, 6

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

# Reversing a list
my_list.reverse()   
print(my_list)  # Output: [6, 5, 4, 3, 2]

# Copying a list
copied_list = my_list.copy()    
print(copied_list)  # Output: [6, 5, 4, 3, 2]

# Clearing a list
my_list.clear()
print(my_list)  # Output: []

## Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0][1])  # Output: 2   

# List methods
my_list = [1, 2, 3, 4, 5]
print(my_list.count(3))  # Output: 1
print(my_list.index(3))  # Output: 2

# List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# List repetition
repeated_list = list1 * 3
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# List membership
print(3 in my_list)  # Output: True
print(10 in my_list)  # Output: False

# List unpacking
a, b, c, d, e = my_list
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# List comprehension with condition
even_numbers = [x for x in my_list if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]

# List comprehension with nested loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]  

# List comprehension with function
def square(x):
    return x ** 2   
squared_list = [square(x) for x in my_list]
print(squared_list)  # Output: [1, 4, 9, 16, 25]    

# List comprehension with multiple conditions
filtered_list = [x for x in my_list if x % 2 == 0 and x > 2]
print(filtered_list)  # Output: [4]

# List comprehension with enumerate
enumerated_list = [(index, value) for index, value in enumerate(my_list)]
print(enumerated_list)  # Output: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]  

# List comprehension with zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_list = [(x, y) for x, y in zip(list1, list2)]
print(zipped_list)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# List comprehension with a function and condition
def is_even(x):
    return x % 2 == 0

even_numbers = [x for x in my_list if is_even(x)]
print(even_numbers)  # Output: [2, 4]

