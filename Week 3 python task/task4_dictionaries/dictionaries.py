# Task 4: Dictionaries in Python

# 1. Creating a student information dictionary
student = {
    "Name": "Vinay",
    "Age": 21,
    "Course": "AI & Data Science",
    "City": "Hyderabad"
}

print("Original Student Information:")
print(student)

# 2. Accessing values
print("\nAccessing Values:")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Course:", student["Course"])
print("City:", student["City"])

# 3. Adding a new key-value pair
student["College"] = "Dhanalakshmi Srinivasan University"

print("\nAfter Adding College:")
print(student)

# 4. Updating values
student["Age"] = 22
student["City"] = "Chennai"

print("\nAfter Updating Values:")
print(student)

# 5. Removing data
student.pop("City")

print("\nAfter Removing City:")
print(student)

# 6. Displaying keys and values
print("\nDictionary Keys:")
print(student.keys())

print("\nDictionary Values:")
print(student.values())

print("\nDictionary Items:")
print(student.items())

# 7. Using dictionary methods
print("\nUsing Dictionary Methods:")

print("Name using get():", student.get("Name"))
print("Age using get():", student.get("Age"))

# Adding or updating multiple key-value pairs
student.update({
    "City": "Chennai",
    "Year": "Final Year"
})

print("\nAfter Using update():")
print(student)

# Finding the number of key-value pairs
print("\nTotal Number of Details:", len(student))

# Displaying each key and value using a loop
print("\nDisplaying All Student Details:")

for key, value in student.items():
    print(key, ":", value)