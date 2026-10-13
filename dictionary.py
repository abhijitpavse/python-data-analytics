# # 02 10 2026


# Create a Python program that stores the marks of 5 students using a dictionary.

# Write a program to:

# Display all students and their marks.
# Ask the user to enter a student's name and display their marks.
# Find and display the student who scored the highest marks.
# Calculate and display the average marks.
# Display students who scored more than 75 marks.
# Add a new student to the dictionary.



# Create an empty dictionary
students = {}


# 1. Take input for 5 students

print("Enter details of 5 students")

for i in range(5):

    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students[name] = marks


# 2. Display all students and marks

print("\n----- All Students and Marks -----")

for name, marks in students.items():
    print(name, ":", marks)


# 3. Search for a student's marks

search_name = input("\nEnter student's name to search: ")

if search_name in students:
    print(search_name, "scored", students[search_name], "marks")
else:
    print("Student not found")


# 4. Find student with highest marks

highest_student = max(students, key=students.get)
highest_marks = students[highest_student]

print("\n----- Highest Marks -----")

print("Student:", highest_student)
print("Marks:", highest_marks)


# 5. Calculate average marks

total_marks = sum(students.values())

average_marks = total_marks / len(students)

print("\n----- Average Marks -----")

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


# 6. Display students scoring more than 75 marks

print("\n----- Students Scoring More Than 75 -----")

for name, marks in students.items():

    if marks > 75:
        print(name, ":", marks)

print("\n----- Students Scoring More Than Average -----")

for name, marks in students.items():

    if marks > average_marks:
        print(name, ":", marks)

# 7. Add a new student

print("\n----- Add New Student -----")

new_name = input("Enter new student name: ")
new_marks = int(input("Enter new student's marks: "))

students[new_name] = new_marks

# 8. Display updated dictionary

print("\n----- Updated Student Details -----")

for name, marks in students.items():
    print(name, ":", marks)

