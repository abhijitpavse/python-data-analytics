# 16 09 2026

# take the input from the user to print the table for any given number 

num = int(input("Enter the number: "))

for i in range(1,11): # this range is making the list from 1 to 10 
    print(num,"*",i,"=",num*i) # print(f"{num}*{i}={num*i}")

# NOTE : defination of for-loop() :for loop is used to perform repeatative task, it works on the number of iteration returned by the iterable

# OR 

num = int(input("Enter the number: "))

print(num,"*",1,"=",num*1)  # print(f"{num}*{1}={num*1}") {} is called placeholder
print(num,"*",2,"=",num*2)
print(num,"*",3,"=",num*3)
print(num,"*",4,"=",num*4)
print(num,"*",5,"=",num*5)
print(num,"*",6,"=",num*6)
print(num,"*",7,"=",num*7)
print(num,"*",8,"=",num*8)
print(num,"*",9,"=",num*9)
print(num,"*",10,"=",num*10)



# h