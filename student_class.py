# 12 10 2026

# make a class of student a student take name age class phone email
# in functions def(study) 
# if course 

class Student:
    def __init__(self, name, email, phone, age, course):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.course = course

    def study(self):
        if self.course == "Python":
            print(f"{self.name} is learning Python for Data Analysis")

        elif self.course == "Java":
            print(f"{self.name} is learning Java for Software Development")

        else:
            print(f"{self.name} is learning {self.course}")


# Creating an object
s1 = Student("Pratik", "pratik@gmail.com", "9876543210", 21, "Python")
s2 = Student("Abhi","abhi@gmail.com","9876543210",21,"Java")

# Calling the function
s1.study()
s2.study()