# # 22 09 2026

# # using while loop
# print("using while")
# i=0
# while(i<=10):
#     print(i)
#     i+=1  #OR i=i+1 
#     # using step count 2 i+=1

# i=10
# while(i>0):
#     print(i)
#     i-=1


password = "admin@123" 
pswd = input("Enter your password: ")
while(pswd!=password):
    print("Incorrect Password")
    pswd = input("RE-Enter your password: ")

print("Welcome")