# 22 09 2026

for i in range(0,10):
    if(i==5):
        continue
    print(i)

# print odd numbers
for i in range(0,10):
    if(i%2==0):
        continue
    print(i)

# print even numbers
for i in range(0,10):
    if(i%2!=0):
        continue
    print(i)

# print all the non prime numbers between 10 to 50

for i in range(10, 51):  # Changed to 51 so 50 is included
    for j in range(2, i):
        if i % j == 0:
            print(i)
            break


for i in range(0,10):
    if(i%2==0):
        continue
    print(i)


# using while loop
print("using while")
i=0
while(i<=10):
    print(i)
    i+=1  #OR i=i+1 
    # using step count 2 i+=1

i=10
while(i>0):
    print(i)
    i-=1


password = "admin@123" 
pswd = input("Enter your password: ")
while(pswd!=password):
    print("Incorrect Password")
    pswd = input("RE-Enter your password: ")

print("Welcome")