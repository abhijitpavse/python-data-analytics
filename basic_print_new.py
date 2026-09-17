# 09 09 2026

# print("Hello Welcome to the Python Session!") # this is used to print the message

# print("Hello \nWelcome to the Python Session!") # this is used to print the message in new line using "\n"

# # now joining two strings using end=""
# print("Hello", end=" ")
# print("Welcome to the Python Session!", end=" ")
# print("Have a nice day!",end=".")

# using sep=""
a = 5
b = 6
c = 7

print(a,b,c)
print(a,end=",")
print(b,end=",")
print(c)
# the above part is to lengthy so we use sep="" which also gives same output

print(a,b,c,sep=",") # sep is used to separate the values & inside "" is used to separate the values based on

print(a,b,c,sep="\n") # \n will be used to print the values in new line

print(a,b,c,sep="\t") # \t will be used to print values in tab format  
print(a,b,c,sep="\t\t\t") # mulitple \t will be used to print multiple tabs



# printing using comparison operator
print(a==5)
print(type(a==5))