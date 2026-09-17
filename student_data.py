# 08 09 2026
# take and input of student name, roll no, marks of 5 subject and calculate total marks, percentage and grade

name = input("Enter your name: ")
roll_no = input("Enter your roll no: ")
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
marks4 = int(input("Enter marks of subject 4: "))
marks5 = int(input("Enter marks of subject 5: "))


print("\n----- Student Details -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Marks:", marks1, marks2, marks3, marks4, marks5)
total_marks = marks1 + marks2 + marks3 + marks4 + marks5
avg_marks = total_marks / 5
print("Average Marks: ", avg_marks)
percentage = (total_marks / 500) * 100
print("Percentage: ", percentage,"%")


# # / same code using list for student marks
# marks = [marks1, marks2, marks3, marks4, marks5]
# total_marks = sum(marks)
# avg_marks = total_marks / 5
# print("Average Marks: ", avg_marks)
# percentage = (total_marks / 500) * 100
# print("Percentage: ", percentage) # /