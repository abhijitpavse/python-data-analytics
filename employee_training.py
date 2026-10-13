# 07 10 2026
# employee training and certificate


employees = {
    "E101": {
        "name": "Rahul",
        "department": "IT",
        "courses": ["Python", "SQL"],
        "skills": {"Python", "SQL", "Git"},
        "rating": 4
    },

    "E102": {
        "name": "Priya",
        "department": "HR",
        "courses": ["Python", "Excel"],
        "skills": {"Python", "Excel", "Communication"},
        "rating": 5
    },

    "E103": {
        "name": "Amit",
        "department": "IT",
        "courses": ["Java", "SQL"],
        "skills": {"Java", "SQL", "Git"},
        "rating": 3
    },

    "E104": {
        "name": "Sneha",
        "department": "Finance",
        "courses": ["Excel", "Power BI"],
        "skills": {"Excel", "Power BI", "SQL"},
        "rating": 4
    }
}


courses = (
    "Python",
    "Java",
    "SQL",
    "Excel",
    "Power BI",
    "React",
    "Spring Boot"
)


# 1. Display Employee Information

print("\n1. Display Employee Information")

for m,n in employees.items():

    print("Id :",m)

    for k,v in n.items():

        print(k,":",v)

    print()


# 2. Search for an Employee

print("\n2. Search for an Employee")

search_id = input("Enter Employee ID: ")

found = False

for m,n in employees.items():

    if m == search_id:

        found = True

        print("Id :",m)

        for k,v in n.items():

            print(k,":",v)

if found == False:
    print("Employee not found")


# 3. Display All Available Courses

print("\n3. Display All Available Courses")

for i in courses:

    print(i)


# 4. Add a Course to an Employee

print("\n4. Add a Course to an Employee")

search_id = input("Enter Employee ID: ")
new_course = input("Enter Course: ")

employee_found = False
course_found = False
already_added = False

for m,n in employees.items():

    if m == search_id:

        employee_found = True

        for i in courses:

            if i == new_course:

                course_found = True

        for k,v in n.items():

            if k == "courses":

                for i in v:

                    if i == new_course:

                        already_added = True

                if course_found == True and already_added == False:

                    v.append(new_course)

                    print("Course added successfully")

                if already_added == True:

                    print("Course already enrolled")


if employee_found == False:

    print("Employee not found")

if employee_found == True and course_found == False:

    print("Course not available")


# 5. Find Unique Courses Being Taken

print("\n5. Find Unique Courses Being Taken")

unique_courses = set()

for m,n in employees.items():

    for k,v in n.items():

        if k == "courses":

            for i in v:

                unique_courses.add(i)


print("Unique Courses:")

for i in unique_courses:

    print(i)


# 6. Find Common Skills

print("\n6. Find Common Skills")

first_id = input("Enter First Employee ID: ")
second_id = input("Enter Second Employee ID: ")

first_skills = set()
second_skills = set()


for m,n in employees.items():

    if m == first_id:

        for k,v in n.items():

            if k == "skills":

                for i in v:

                    first_skills.add(i)


    if m == second_id:

        for k,v in n.items():

            if k == "skills":

                for i in v:

                    second_skills.add(i)


common_skills = first_skills.intersection(second_skills)

print("Common Skills:")

for i in common_skills:

    print(i)


# 7. Find All Technical Skills

print("\n7. Find All Technical Skills")

all_skills = set()

for m,n in employees.items():

    for k,v in n.items():

        if k == "skills":

            for i in v:

                all_skills.add(i)


print("All Technical Skills:")

for i in all_skills:

    print(i)


# 8. Department-wise Employee List

print("\n8. Department-wise Employee List")

department_employees = {}

for m,n in employees.items():

    department = ""
    name = ""

    for k,v in n.items():

        if k == "department":

            department = v

        if k == "name":

            name = v


    if department not in department_employees:

        department_employees[department] = []


    department_employees[department].append(name)


for m,n in department_employees.items():

    print("Department :",m)

    for i in n:

        print(i)

    print()


# 9. Course-wise Employee List

print("\n9. Course-wise Employee List")

course_employees = {}

for m,n in employees.items():

    name = ""

    for k,v in n.items():

        if k == "name":

            name = v

        if k == "courses":

            for i in v:

                if i not in course_employees:

                    course_employees[i] = []

                course_employees[i].append(name)


for m,n in course_employees.items():

    print("Course :",m)

    for i in n:

        print(i)

    print()


# 10. Find the Most Popular Course

print("\n10. Find the Most Popular Course")

course_count = {}

for m,n in employees.items():

    for k,v in n.items():

        if k == "courses":

            for i in v:

                if i not in course_count:

                    course_count[i] = 0

                course_count[i] = course_count[i] + 1


max_count = 0
max_course = ""


for m,n in course_count.items():

    if n > max_count:

        max_count = n
        max_course = m


print("Most Popular Course :",max_course)
print("Number of Employees :",max_count)


# 11. Find Employees with a Particular Skill

print("\n11. Find Employees with a Particular Skill")

search_skill = input("Enter Skill: ")


for m,n in employees.items():

    employee_name = ""
    skill_found = False

    for k,v in n.items():

        if k == "name":

            employee_name = v

        if k == "skills":

            for i in v:

                if i == search_skill:

                    skill_found = True


    if skill_found == True:

        print("Id :",m)
        print("Name :",employee_name)


# 12. Compare Two Employees

print("\n12. Compare Two Employees")

first_id = input("Enter First Employee ID: ")
second_id = input("Enter Second Employee ID: ")


first_courses = set()
second_courses = set()

first_skills = set()
second_skills = set()


for m,n in employees.items():

    if m == first_id:

        for k,v in n.items():

            if k == "courses":

                for i in v:

                    first_courses.add(i)

            if k == "skills":

                for i in v:

                    first_skills.add(i)


    if m == second_id:

        for k,v in n.items():

            if k == "courses":

                for i in v:

                    second_courses.add(i)

            if k == "skills":

                for i in v:

                    second_skills.add(i)


common_courses = first_courses.intersection(second_courses)

common_skills = first_skills.intersection(second_skills)

first_unique_courses = first_courses.difference(second_courses)

second_unique_courses = second_courses.difference(first_courses)


print("Common Courses:")

for i in common_courses:

    print(i)


print("Common Skills:")

for i in common_skills:

    print(i)


print("Courses Unique to First Employee:")

for i in first_unique_courses:

    print(i)


print("Courses Unique to Second Employee:")

for i in second_unique_courses:

    print(i)


# 13. Performance Analysis

print("\n13. Performance Analysis")

rating_employees = {}


for m,n in employees.items():

    employee_name = ""
    rating = 0

    for k,v in n.items():

        if k == "name":

            employee_name = v

        if k == "rating":

            rating = v


    if rating not in rating_employees:

        rating_employees[rating] = []


    rating_employees[rating].append(employee_name)


for m,n in rating_employees.items():

    if m == 5:

        print("Rating :",m)
        print("Category : Outstanding")

    elif m == 4:

        print("Rating :",m)
        print("Category : Excellent")

    elif m == 3:

        print("Rating :",m)
        print("Category : Good")

    elif m == 2:

        print("Rating :",m)
        print("Category : Needs Improvement")

    elif m == 1:

        print("Rating :",m)
        print("Category : Poor")


    for i in n:

        print(i)

    print()


# 14. Find the Top Performer

print("\n14. Find the Top Performer")

max_rating = 0


for m,n in employees.items():

    for k,v in n.items():

        if k == "rating":

            if v > max_rating:

                max_rating = v


print("Highest Rating :",max_rating)

print("Top Performer:")


for m,n in employees.items():

    for k,v in n.items():

        if k == "name":

            employee_name = v

        if k == "rating":

            if v == max_rating:

                print("Id :",m)
                print("Name :",employee_name)


# 15. Count Employee Courses

print("\n15. Count Employee Courses")

employee_course_count = {}


for m,n in employees.items():

    employee_name = ""
    course_count = 0

    for k,v in n.items():

        if k == "name":

            employee_name = v

        if k == "courses":

            for i in v:

                course_count = course_count + 1


    employee_course_count[employee_name] = course_count


for m,n in employee_course_count.items():

    print(m,":",n)


max_courses = 0


for m,n in employee_course_count.items():

    if n > max_courses:

        max_courses = n


print("Employee(s) with Most Courses:")


for m,n in employee_course_count.items():

    if n == max_courses:

        print(m)


# 16. Find Employees Who Need More Training

print("\n16. Find Employees Who Need More Training")


for m,n in employees.items():

    employee_name = ""
    course_count = 0
    rating = 0


    for k,v in n.items():

        if k == "name":

            employee_name = v

        if k == "courses":

            for i in v:

                course_count = course_count + 1

        if k == "rating":

            rating = v


    if course_count < 2 or rating <= 3:

        print("Id :",m)
        print("Name :",employee_name)