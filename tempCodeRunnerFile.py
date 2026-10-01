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