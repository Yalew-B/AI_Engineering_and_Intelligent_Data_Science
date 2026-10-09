# Sets in Python
# A set is a collection of unique elements.
# Sets are written with curly brackets.
my_set: set[int] = {1, 2, 3, 4, 5}
print(my_set)

# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
my_set.remove(1)
print(my_set)  # Output: {2, 3, 4, 5, 6}

# Set operations
set1: set[int] = {1, 2, 3}
set2: set[int] = {3, 4, 5}

# Union of sets
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Difference of sets
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Checking if an element is in a set
print(3 in my_set)  # Output: True

# Length of a set
print(len(my_set))  # Output: 5

# Iterating through a set
for item in my_set:
    print(item)
    
# Set comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}

# Clearing a set
my_set.clear()
print(my_set)  # Output: set()
