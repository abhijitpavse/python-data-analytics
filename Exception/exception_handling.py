# 22 10 2026


# Exception           |  Cause                     |
# --------------------|----------------------------|
# 'ZeroDivisionError' | Division by zero           |
# 'ValueError'        | Invalid conversation       |
# 'IndexError'        | Invalid index              |
# 'NameError'         | Variable not found         |
# 'TypeError'         | Invalid data type operation|
# 'FileNotFoundError' | File Does not Exist        | 

try:
    num = int(input("Enter a number:"))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Exception an integer input")


try:
    list_fruits = ["apple","banana","peru"]
    for i in range(0,4):
        print(list_fruits[i])
except IndexError:
    print(f"the index {i} does not exist")



# combibation of above two codes

try:
    num = int(input("Enter a number:"))
    result = 10 / num
    print(result)
    list_fruits = ["apple","banana","peru"]
    for i in range(0,4):
        print(list_fruits[i])
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Exception an integer input")
except IndexError:
    print(f"the index {i} does not exist")
except NameError:
    print("the list with specified name does not exist")




