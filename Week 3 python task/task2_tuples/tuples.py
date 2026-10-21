# Task 2: Tuples in Python
# 1. Creating a tuple
student = ("Vinay", 21, "AI & Data Science", "Hyderabad")
print("Original Tuple:", student)
# 2. Accessing elements using indexing
print("\nAccessing Elements:")
print("Student Name:", student[0])
print("Student Age:", student[1])
print("Student Course:", student[2])
print("Student City:", student[3])
# 3. Tuple slicing
print("\nTuple Slicing:")
print("First Two Elements:", student[0:2])
print("Course and City:", student[2:4])
# 4. Finding the length
print("\nLength of Tuple:", len(student))
# 5. Basic tuple operations
another_tuple = ("Python", "Data Structures")

combined_tuple = student + another_tuple

print("\nCombined Tuple:", combined_tuple)
print("Repeated Tuple:", another_tuple * 2)

# Checking whether an element exists
print("Is Python Present?", "Python" in combined_tuple)