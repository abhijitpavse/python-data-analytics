# x = int(input("Enter the value of x:"))
# print(type(x))
# y = int(input("Enter the value of y:"))
# print(type(y))

# print("The addition of 'x' and 'y' is:",x+y)

# NOTE: for the same program if we dont mension int., or any other data type it will be considered as string 
# and it will just put the values infront of them

# WAP to take user inpur from the user name, age, date of birth, hight, weight and calculate bmi 
from datetime import datetime

# Take input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

dob_input = input("Enter your date of birth (DD-MM-YYYY): ")
dob = datetime.strptime(dob_input, "%d-%m-%Y").date()

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display details
print("\n----- User Details -----")
print("Name:", name)
print("Age:", age)
print("Date of Birth:", dob)
print("Height:", height, "m")
print("Weight:", weight, "kg")
print("BMI:", round(bmi, 2))
print(type(bmi))