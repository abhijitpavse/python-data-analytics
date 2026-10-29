# 01 10 2026



# tuple:

student_data = (10, 'Soham', 'Python', 40000.00) # duplicate values are allowed , stores combination of different data types
#student_data[1] = 'Shubham' # this will give error as tuple is immutable (not allowed)

# for multiple records we use list(which is called list of tuples)
student_data = [(10, 'Soham', 'Python', 40000.00),(11, 'Sohani', 'Python', 40000.00)]
#  print student_data using for loop

for student in student_data:
    print(student)

# without using loop
print(student_data)



# sets: stores only unique values
    # sequence does not matter in set  
student_id = {101,102,103,104,101}

print(student_id)

# print using for loop
for id in student_id:
    print(id)

# adding values in the set

print("After adding 108")
student_id.add(108)
print(student_id)

for id in student_id:
    print(id)

# removing values in the set

print("After removing 101")  # this will remove both 101 value bcz its always take only unique val
student_id.remove(101)
print(student_id)

for id in student_id:
    print(id)

# not using for loop
print("Not using loop")
print(student_id)


# print set of tuples
print("Print set of tuples")
student_data = [(10, 'Soham', 'Python', 40000.00),(10, 'Soham', 'Python', 40000.00)]
# if here data is same or duplicate it will not print

student_set = set(student_data)
# print(student_set)
# using for loop
for student in student_set:
    print(student)



# dictionary:
#     key   :   value  (pair of key and value)
  
student_details = {
    "id":101,    # id is key and 101 is value
    "name":"Soham",
    "marks":84
}
print("Student name: ",student_details["name"]) # accessing the name through the key
# print("id:",student_details["id"])
# print("name:",student_details["name"])
# print("course:",student_details["course"])
# print("fees:",student_details["fees"])

# now adding new record
student_details["age"] = 23


print("Student age: ",student_details["age"])

print("Using for loop")

for m,n in student_details.items():
    print(m,":",n)  # m is key & n is value  so this is the format of dictionary

# for multilple records / values dictionary
student_details = {
    "id":[101,102,103,104,105],    # id is key and 101 is value
    "name":["Soham", "Shubham", "Adesh", "Mahesh", "Hemant"],
    "marks":[90,80,70,60,40]
}

# Using for loop And seperate key and value
print("Using for loop And seperate key and value")
student_details = {
    "id":[101,102,103,104,105],    # id is key and 101 is value
    "name":["Soham", "Shubham", "Adesh", "Mahesh", "Hemant"],
    "marks":[90,80,70,60,40]
}

for i in range(0,5):
    for m,n in student_details.items():
        print(m,":",n[i])

print("ID",      "Name",      "Marks")
for i in range(0,5):
    print(student_details["id"][i],student_details["name"][i],student_details["marks"][i]) 

# upar wala pratik ka doubt tha ki aisa kaise print karu



