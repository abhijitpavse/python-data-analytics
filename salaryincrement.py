# WAP to take user input as salary from employee and increment salary
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
# othrwise, no additinaol bonus

name = input("Enter your name: ")
salary =float(input("Enter your salary: "))
experience = float(input("Enter your experience: "))
rating = float(input("Enter your rating: "))


if rating == 5:
    if experience >= 5:
        increment = (salary * 20) / 100 # for same code we can also use 'salary * 0.2' no need to use '/'
    else:
        increment = (salary * 15) / 100
elif rating == 4:
    if experience >= 5:
        increment = (salary * 15) / 100
    else:
        increment = (salary * 10) / 100
elif rating == 3:
    if experience >= 5:
        increment = (salary * 10) / 100
    else:
        increment = (salary * 7) / 100
elif rating == 2:
    if experience >= 5:
        increment = (salary * 5) / 100
    else:
        increment = (salary * 3) / 100
else:
    increment = 0

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
