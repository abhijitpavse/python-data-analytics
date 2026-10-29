# 21 10 2026

# mode          meaning
# -----------------------
# "r"           read 
# "w"           write (overwrites file)
# "a"           append
# "x"           create new file
# "t"           text mode(default)
# "b"           binary mode


# file = open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.txt","x")
# file.write("Hello Students")
# file.write("Welcome to Python")
# file.write("We are doing advanced Python")
# file.write("Practice file handling")

# # file.writelines(["Hello "])

# file.close()


list_of_strings = ["Hello students","welcome to python","we are doing advanced python"]
with open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.txt","w") as f:
    f.writelines(list_of_strings)

f.close()

# file = open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.txt")
# content = file.read()
# print(content)
# file.close()

# content = file.readline()

try:
    with open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data1.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not Exist")









