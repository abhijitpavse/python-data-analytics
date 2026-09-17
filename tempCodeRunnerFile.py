num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check whether num1 is less than num2
if num1 < num2:

    print("Even numbers:")
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i)

    print("\nOdd numbers:")
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(i)

else:
    print("Invalid input! First number should be less than second number.")