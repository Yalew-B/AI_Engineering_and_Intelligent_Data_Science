# Tuples in Python
# A tuple is a collection of items that are ordered and unchangeable.
# Tuples are written with parentheses.
my_tuple: tuple[int, int, int] = (1, 2, 3)
print(my_tuple)

# Accessing elements in a tuple
# Accessing elements in a tuple is done using indexing, similar to lists.
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 3

# Slicing a tuple
print(my_tuple[1:3])  # Output: (2, 3)

# Length of a tuple
print(len(my_tuple))  # Output: 3

# Iterating through a tuple
for item in my_tuple:
    print(item)

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Tuple methods
print(my_tuple.count(2))  # Output: 1
print(my_tuple.index(2))  # Output: 1
