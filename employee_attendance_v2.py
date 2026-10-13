#  05 10 2026


employees = {
    "E101": {
        "name": "Rahul",
        "department": "IT",
        "attendance": [22, 20, 21, 23],
        "rating": 4
    },

    "E102": {
        "name": "Priya",
        "department": "HR",
        "attendance": [24, 23, 22, 24],
        "rating": 5
    },

    "E103": {
        "name": "Amit",
        "department": "IT",
        "attendance": [18, 20, 19, 21],
        "rating": 3
    },

    "E104": {
        "name": "Sneha",
        "department": "Finance",
        "attendance": [24, 22, 24, 23],
        "rating": 5
    }
}


# max_rating = 0
# for m,n in employees.items():
#     print("id",":",m)

# # for k,v in n.items():
# #     if (k=="attendance"):
# #         print(k,":")
# #         for k in v:
# #             print(k)
# #             for i in v:
# #                 att_sum+=i
# #                 print(i)
# #             print("Total Attendance:",att_sum)    
# #     else:
# #         print(k, ":", v)        
#     att_sum=0  
#     for k,v in n.items():
#         if (k=="attendance"):
#             # print(k,":")
#             for i in v:
#                 att_sum+=i
#                 # print(i)
#             print("Total Attendance:",att_sum)
#             print("Average Attendace:", att_sum/len(v))
#         # else:
#         #     print(k, ":", v)


# #   4. find the best employee based o rating
# for m,n in employees.items():


#     for k,v in n.items():
#         if (k=="rating"):
#             if (v>max_rating):
#                 # print("id with max rating:",m)
#                 max_rating=v
# print(max_rating)



# 1. Display Employee Details

print("\n1. Display Employee Details")
for m,n in employees.items():
    print("Id :",m)

    for k,v in n.items():
        print(k,":",v)

    print()

# 2. Calculate Total Attendance

print("\n2.Calculate Total Attendance")
for m,n in employees.items():
    print("Id :",m)

    alt_sum=0

    for k,v in n.items():
        if (k =="attendance"):
            for i in v:
                alt_sum+=i

            print("Sum of Attendance:",alt_sum)



print("\n3. Calculate Average Attendance")
average_attendance = {}
for m,n in employees.items():
    print("Id :",m)

    alt_sum=0

    for k,v in n.items():
        if (k =="attendance"):
            for i in v:
                alt_sum+=i

            print("Sum of Attendance:",alt_sum)
            print("Average Attendance:",alt_sum/len(v))

            average_attendance[m]=alt_sum/len(v)

print(average_attendance)
# # 4. Find the Best Employee
# print("\n4. Find the Best Employee")

# highest_rating=0
# highest_average=0
# best_id=""

# for m,n in employees.items():

#     rating=0
#     alt_sum=0
#     average=0

#     for k,v in n.items():

#         if (k=="rating"):
#             rating=v

#         if (k=="attendance"):
#             for i in v:
#                 alt_sum+=i

#             average=alt_sum/len(v)

#     if (rating > highest_rating):
#         highest_rating=rating
#         highest_average=average
#         best_id=m

#     elif (rating == highest_rating):
#         if (average > highest_average):
#             highest_average=average
#             best_id=m

# print("Best Employee:",best_id)
# print("Highest Rating:",highest_rating)
# print("Average Attendance:",highest_average)



print("\n4. Find the Best Employee")
max_rating = 0
max_average = 0
max_employee = []
max_r_att = 0
max_r_att_emp = " "

for m,n in employees.items():

    alt_sum = 0
    # average = 0

    for k,v in n.items():

        if (k == "rating"):

            if (v > max_rating):
                max_rating = v

for m,n in employees.items():
    for k,v in n.items():
        if (k == "rating" and v == max_rating ):
            max_employee.append(m)
if len(max_employee) > 1:
    for emp in max_employee:
        if average_attendance[emp] >= max_r_att:
            max_r_att = average_attendance[emp]
            max_r_att_emp = emp

    print("Best Employee:",max_r_att_emp)
    print("Highest Rating:",max_rating)
    print("Average Attendance:",max_r_att)
else:
    print("Best Employee:",max_employee[0])
    print("Highest Rating:",max_rating)




print("\n5. Identify Employees at Risk")

for m,n in employees.items():

    alt_sum = 0
    average = 0
    rating = 0

    for k,v in n.items():

        if (k == "attendance"):
            for i in v:
                alt_sum += i

            average = alt_sum / len(v)

        if (k == "rating"):
            rating = v

    if (average < 20 or rating <= 2):
        print("Employee at Risk:",m)


print("\n6. Department wise employee count")

employees_count = {}

# for m,n in employees.items():
#     # department = n["department"]
#     for k,v in n.items():
#         if (k == "department" and v not in employees_count):
#             employees_count[v] = 1

#         elif (k == "department" and v in employees_count):
#             employees_count[v] += 1
# print("Department wise employee count:",employees_count)

#OR

for m,n in employees.items():
    for k,v in n.items():
        if k=="department":
            if v in employees_count:
                employees_count[v]+=1
            else:
                employees_count[v]=1
print("Department wise employee count:",employees_count)


# print("\n7. Department-wise Average Attendance")
# add same department people in on place

# department_avg_attendance = {}


# for m,n in employees.items():
#     sum_attendance = 0
#     average_attendance = 0

#     for k,v in n.items():
#         if k == "attendance":
#             for i in v:
#                 sum_attendance += i
#             average_attendance = sum_attendance / len(v)
#         if k == "department":
#             if v not in department_avg_attendance:
#                 department_avg_attendance[v] = []
#                 department_avg_attendance[v].append(average_attendance)
#             else:
#                 department_avg_attendance[v].append(average_attendance)

# for k,v in department_avg_attendance.items():
#     average_attendance = 0
#     for i in v:
#         average_attendance += i
#     average_attendance = average_attendance / len(v)
#     department_avg_attendance[k] = average_attendance
# print("Department-wise Average Attendance:",department_avg_attendance)

print("\n7. Department-wise Average Attendance")

# Add employees belonging to the same department in one place
department_avg_attendance = {}

for employee_id, employee_data in employees.items():

    # Get department
    department = employee_data["department"]

    # Get attendance
    attendance = employee_data["attendance"]

    # Calculate employee's average attendance
    total_attendance = 0

    for days in attendance:
        total_attendance += days

    average_attendance = total_attendance / len(attendance)

    # Add average attendance to department
    if department not in department_avg_attendance:
        department_avg_attendance[department] = []

    department_avg_attendance[department].append(average_attendance)


# Calculate department-wise average
final_department_average = {}

for department, averages in department_avg_attendance.items():

    total = 0

    for average in averages:
        total += average

    department_average = total / len(averages)

    final_department_average[department] = department_average


print("Department-wise Average Attendance:", final_department_average)



# 8. Performance Categories 
    # 5 = Outstanding, 4 = Excellent, 3 = Good, 2 = Needs Improvement, 1 = Poor.

print("\n8. Performance Categories")

for m,n in employees.items():
    for k,v in n.items():
        if (k == "rating"):
            if (v == 5):
                n[k] = "Outstanding"
            elif (v == 4):  
                n[k] = "Excellent"
            elif (v == 3):
                n[k] = "Good"
            elif (v == 2):
                n[k] = "Needs Improvement"
            elif (v == 1):
                n[k] = "Poor"

print(employees)


# 9. Add a New Employee 
# Ask for Employee ID, Name, Department, attendance for 4 months, and rating, then add the employee.


print("\n. 9. Add a New Employee")

new_id = input("Enter Employee ID: ")
new_name = input("Enter Employee Name: ")
new_department = input("Enter Department: ")
new_attendance = []
new_rating = 0

for month in range(1, 5):
    value = int(input("Enter attendance for month " + str(month) + ": "))
    new_attendance.append(value)

new_rating = int(input("Enter rating: "))

employees[new_id] = {
    "name": new_name,
    "department": new_department,
    "attendance": new_attendance,
    "rating": new_rating
}

print(employees)


# 10. Update Attendance 
# Ask for an employee ID, month number, and new attendance value, then update that attendance.

print("\n10. Update Attendance")

id = input("Enter Employee ID: ")

if id in employees:
    month = int(input("Enter month number (1-4): "))
    if month < 1 or month > 4:
        print("Invalid month number.")
        exit()
    attendance = int(input("Enter new attendance value: "))
    for m,n in employees.items():
        if m == id:
            for k,v in n.items():
                if k == "attendance":
                    n[k][month-1] = attendance

print(employees)


# 11 12 remaining..