# 04 09 2026

print("Welcome to the Python Session!")


# variable (a) and its value is 10
# variable is container that can store values it represent memory location which can change its value within the program
x = 10
print("The value of a is:",x) # print is used to print the value  And in "" is string (message)


y = 20
print("The value of y is:",y)

print("The addition of 'x' and 'y' is:",x+y)
print("The subtraction of 'x' and 'y' is:",x-y)
print("The multiplication of 'x' and 'y' is:",x*y)
print("The devision of 'x' and 'y' is:",x/y)
print("The modulos of 'x' and 'y' is:",x%y)
print("The modulos of 'x' and 'y' is:",x**3)

a=5
b=6
print(type(a/b)) # continues division
print(type(a//b)) # floor division




# using multiple arguments " "
print("The addition of", x, "and", y, "is:",x+y)
print("The subtraction of", x, "and", y, "is:",x-y)
print("The multiplication of", x, "and", y, "is:",x*y)
print("The devision of", x, "and", y, "is:",x/y)
print("The modulos of", x, "and", y, "is:",x%y)


# using f string format method
# using \n and using seperate print statement we can add new line
print(f"The addition of {x} and {y} is:\n{x+y}")
print(f"The addition of {x} and {y} is:")
print(x+y)


# joining of two statements
print(f"The addition of {x} and {y} is:",end=" ") # end is parameter
print(x+y)

print(f"The addition of {x} and {y} is",end=": ") # end is parameter
print(x+y)


# 07 09 2026
# To know data type
# x = 10
# print(type(x))

# x = 10.5
# print(type(x))

# x = "Python"
# print(type(x))



# to change data types
num = 42

# Method 1: Using str()
text = str(num)
print(type(text))

# Method 2: Using int()
num = int("42")
print(type(num))

