# 17 09 2026 Home Work

# WAP to print even odd numbers between range 10 to 20 
# num1 =10
# num2 =20
# num1<num2 if true
# start the loop with range num1,num2+1

# for i in range(10,21):
#     if i%2==0:  
#         print(i,"is even number")
#     else:
#         print(i,"is odd number")    


#OR

# write code with taking input from user and num 1 should be less than num2


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for i in range(num1,num2+1):
    if i%2==0:  
        print(i,"is even number")
    # if i%2!=0: # if i%2==1: 
    else:
        print(i,"is odd number")


# OR

# write code with taking input from user and num 1 should be less than num2 and print nums even and then odd to seperate places

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