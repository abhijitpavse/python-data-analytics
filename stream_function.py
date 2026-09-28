# 28 09 2026

# make 4 functions:
# function 1 user input : id,name,email,phone
   # stream: 1.Science, 2.Arts, 3.Commerce

# function 2: if user choice is: Science
                                #  print subjects: Physics, chemistry, biology, maths

# if user choice is Arts :
                        # print subjects: marathi, hindi, social science, EVS

# # if user choice is Commerce :
                        # print subjects: Accounts, Audit, Economics, Secretarial Practice

# function 3: take input for user marks according to the subjects of stream

# function 4: display all the details


def user_input():
    id = int(input("Enter your id: "))
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = int(input("Enter your phone: "))
    return id,name,email,phone


def streams():
    print("\n1.Science")
    print("2.Arts")
    print("3.Commerce")
    choice = int(input("Enter your choice 1,2,3: "))
    return choice 

def subjects(choice):
    if choice == 1:
        subject_list = ["Physics","Chemistry","Biology","Mathematics"]
    elif choice == 2:
        subject_list = ["Marathi","Law","Social Science","EVS"]
    elif choice == 3:
        subject_list = ["Accounts","Audit","Economics","Secretarial Practice"]
    else:
        subject_list = []
        print("Invalid Choice")
    return subject_list

# enter your marks for selected subjects from stream
def marks(subject_list):
    marks_list ={}
    for subject in subject_list:
        marks = int(input(f"Enter your marks for {subject}: "))
        marks_list[subject] = marks
    return marks_list


def display_data(id, name, email, phone, choice, subject_list, marks_list):

    print("\n========== STUDENT DETAILS ==========")

    print("ID:", id)
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)

    if choice == 1:
        print("Stream: Science")

    elif choice == 2:
        print("Stream: Arts")

    elif choice == 3:
        print("Stream: Commerce")

    print("\nSubjects and Marks:")

    for subject in subject_list:
        print(subject, ":", marks_list[subject])



# # Main program

id, name, email, phone = user_input()

choice = streams()
subject_list = subjects(choice)
marks_list = marks(subject_list)
display_data(id,name,email,phone,choice,subject_list,marks_list)