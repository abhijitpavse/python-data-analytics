# 23 09 2026


# Problem: Write a program that continuously asks the user to enter numbers. 
# The loop should keep running until the user types 0 (this is called a sentinel value). 
# Once 0 is entered, the program should print the total sum of all entered numbers.


total = 0
while True:
    num = int(input("Enter a number (or 0 to stop): "))
    if num == 0:
        break
    total += num

print("Total sum:", total)
