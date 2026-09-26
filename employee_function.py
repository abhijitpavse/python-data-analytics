# 26 09 2026

# WAP using functions to take user input as salary from employee and increment salary
# rating 5
# experience >= 5 years -> 20% increment
# experience < 5 years -> 15% increment
# rating 4
# experience >= 5 years -> 15% increment
# experience < 5 years -> 10% increment
# rating 3
# experience >= 5 years -> 10% increment
# experience < 5 years -> 7% increment
# rating 2
# experience >= 5 years -> 5% increment
# experience < 5 years -> 3% increment
# rating 1
# no increment

# 3. additional bonus 
# after calculating the increment,
# if the employee has experience more than 10 years and rating
# is4 or 5, then give additional 25000 bonus
# othrwise, no additinal bonus 

name = input("Enter your name: ")
salary = float(input("Enter your salary: "))
experience = float(input("Enter your experience: "))
rating = float(input("Enter your rating: "))


def increment_salary(salary, experience, rating):
    if rating == 5:
        if experience >= 5:
            increment = salary * 0.2
        else:
            increment = salary * 0.15
    elif rating == 4:
        if experience >= 5:
            increment = salary * 0.15
        else:
            increment = salary * 0.1
    elif rating == 3:
        if experience >= 5:
            increment = salary * 0.1
        else:
            increment = salary * 0.07
    elif rating == 2:
        if experience >= 5:
            increment = salary * 0.05
        else:
            increment = salary * 0.03
    else:
        increment = 0

    return increment

increment = increment_salary(salary, experience, rating)

if experience >= 10 and (rating ==4 or rating == 5):
    additional_bonus = 25000
else:
    additional_bonus = 0

total_salary = salary + increment + additional_bonus

print(f"Name: {name}")
print(f"Salary: {salary}")
print(f"Experience: {experience}")
print(f"Rating: {rating}")
print(f"Increment: {increment}")
print(f"Salary with Increment: {salary + increment}")
print(f"Additional Bonus: {additional_bonus}")
print(f"Total Salary: {total_salary}")  