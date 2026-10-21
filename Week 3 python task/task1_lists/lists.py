#task1 = lists in python
# 1. Creating a list
students = ["Arun", "Bala", "Charan", "Divya", "Ezhil"]

print("Original List:", students)

# 2. Accessing elements
print("\nAccessing Elements:")
print("First student:", students[0])
print("Third student:", students[2])

# 3. Adding elements
students.append("Farhan")
print("\nAfter Adding an Element:", students)

# 4. Updating elements
students[1] = "Bharath"
print("\nAfter Updating an Element:", students)

# 5. Removing elements
students.remove("Charan")
print("\nAfter Removing an Element:", students)

# 6. Sorting the list
students.sort()
print("\nAfter Sorting the List:", students)