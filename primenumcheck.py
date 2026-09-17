# 17 09 2026

# take input from the user and check if the number is prime or not

# 1 Neither Only has 1 factor (prime numbers must have exactly 2 factors).
# 2 Prime Divisible only by 1 and 2 (the only even prime number).

num = int(input("Enter the number: "))

if num ==1:
    print(num,"is neither prime nor composite")
elif num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num,"is not a prime number, Composite number")
            break
    else:
        print(num,"is a prime number")
