# print light bill using function
# using different functions to calculate the rate of unit,
# rate: 0-100 is 5rs p/u
# rate: 101-200 is 7rs p/u 
# rate: 201 and above is 10rs p/u
# if bill amount is greater than 3000 then apply 10% surcharge
# for units and surcharge and final print make 3 different functions
# ask user for units


unit = int(input("Enter the number of units: "))

def calculate_rate(unit):
    if unit <= 100:
        return 5
    elif unit <= 200:
        return 7
    else:
        return 10
# surcharge
def calculate_surcharge(bill):
    if bill > 3000:
        return bill * 0.1
    else:
        return 0

bill = unit * calculate_rate(unit)
surcharge = calculate_surcharge(bill)
# print_bill(bill, surcharge)

# print bill and surcharged amount with final amount
def print_bill(bill, surcharge):
    print("Bill amount:", bill)
    # print(f"Bill amount:, {bill} with {unit} units")
    if surcharge == 0:
        print("No surcharge applied")
    else:
        print(f"Surcharge applied is {surcharge} with 10% rate")
    # print(f"Your bill amount is {bill} and surcharge rate is {calculate_rate(unit)}")
    # print("Surcharged amount:", surcharge)
    print(f"Final amount: {bill + surcharge}")

# bill = unit * calculate_rate(unit)
# surcharge = calculate_surcharge(bill)
print_bill(bill, surcharge)