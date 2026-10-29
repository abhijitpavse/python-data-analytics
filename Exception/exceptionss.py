
# 23 10 2026



try:
    num = int(input("Enter a number:"))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Please retry with a numeric value")
except:
    print("Something went wrong")
else:
    print("Division was successful")
finally:
    print("Program exited")



try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise Exception("You must be 18 or above")

    name = input("Enter your name: ")
    print(name,"is Eligible")

except Exception as e:
    print(e)

try:
    sal = int(input("salary: "))
    if sal < 0:
        raise ValueError("Salary cannot be negative")

except ValueError as v:
    print(v)  
    
# # OR
# sal = int(input("salary: "))
# if sal < 0:
#     raise ValueError("Salary cannot be negative")

# except ValueError as v:
#     print(v)