# Task 3: Sets in Python

# 1. Creating a set
numbers = {10, 20, 30, 20, 10}

print("Original Set:", numbers)

# 2. Removing duplicate values
numbers_list = [10, 20, 30, 20, 10]
unique_numbers = set(numbers_list)

print("\nList with Duplicates:", numbers_list)
print("Set without Duplicates:", unique_numbers)

# 3. Adding and removing elements
numbers.add(40)
print("\nAfter Adding 40:", numbers)
numbers.discard(20)
print("After Removing 20:", numbers)

# Creating two sets for set operations
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

print("\nSet A:", set_a)
print("Set B:", set_b)

# 4. Union
print("\nUnion:", set_a.union(set_b))

# 5. Intersection
print("Intersection:", set_a.intersection(set_b))

# 6. Difference
print("Difference (A - B):", set_a.difference(set_b))
print("Difference (B - A):", set_b.difference(set_a))