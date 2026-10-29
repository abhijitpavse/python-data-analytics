# 22 10 2026

# mode          meaning
# -----------------------
# "r"           read 
# "w"           write (overwrites file)
# "a"           append
# "x"           create new file
# "t"           text mode(default)
# "b"           binary mode



# ======================
# 1. READ MODE ("r")
# ======================
print("Read Mode")
try:
    file = open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.txt","r")
    content = file.read()
    print("File Content:",content)
    file.close()
except FileNotFoundError:
    print("File does not exist yet.")



# ======================
# 2. WRITE MODE ("w")
# ======================
print("\nWrite Mode")
file = open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.txt","w") # creates or overwrites file
file.write("Hello Students\n")
file.write("This is write mode\n")
file.close()
print("Data written using write mode.")



# ======================
# 3. APPEND MODE ("a")
# ======================
print("\nAppend Mode")
file = open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.txt","a") # adds at end file
file.write("This line is appended\n")
file.close()
print("Data appended.")



# ======================
# 4. EXCLUSIVE MODE ("x")
# ======================
print("\nCreate Mode")
try:
    file = open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.txt","x") # creates new file
    file.write("File crated using x mode")
    file.close()
    print("newfile.txt created.")
except FileExistsError:
    print("newfile.txt already exists.")


# ======================
# 5. TEXT MODE ("t") -- default
# ======================
print("\nText Mode")
file = open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.txt","rt") # same as "r"
print("Text mode read: ",file.read())
file.close()



# ======================
# 6. BINARY MODE ("b")
# ======================
print("\nBinary Mode")

# writes binary
file = open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.bin","wb")
file.write(b"Hello binary world\n")
file.write(b"Trying binary")
file.close()
print("Data written using binary mode.")


# reads binary
file = open("C:/Users/abhijit/Documents/SPRK Python Codes2/File_Handling/data.bin","rb")
data = file.read()
print("Binary data: ",data)
file.close()