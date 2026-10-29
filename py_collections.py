# 29 09 2026


# list  : denoted using []   # list is mutable
# tuple : denoted using ()   # tuple is immutable
# set   : denoted using {}
# dict  : denoted using {}


# list
# to access the elements in the list use index number we can access the elements in the list
a = 10
b = 20
c = 30

numbers = [10, 20, 30]   # list of numbers stores a single datatype
print("a",a)
print("The entire list: ",numbers)
# to access the elements in the list seperatly 
print("The first element: ",numbers[0])
print("The second element: ",numbers[1])
print("The third element: ",numbers[2])

# now for arethmatic operations we can not use 'numbers+1' like this
# format for that we need to do with index 'numbers[0]+1'
print("Adding 1 to first element: ",numbers[0]+1)



# list of fruits

fruits = ["Apple", "Banana", "Orange"]

print("The entire list: ",fruits)
print("The first element: ",fruits[0])
print("The second element: ",fruits[1])
print("The third element: ",fruits[2])


# now for arethmatic operations we can not use 'fruits+1' like this
# format for that we need to do with index 'fruits[0]+1'
# print("Adding 1 to first element: ",fruits[0]+1)


# now if we want to add new eleement into existing list we use append()
numbers.append(50) # by default it will add at the end of the list
print("The entire list after adding 50: ",numbers)

# now if we want to delete the element from the list we use remove()
numbers.remove(30) # by default it will remove the first occurance of the element
print("The entire list after removing 30: ",numbers)
# print(numbers[3])  # this will give error bcz there is no element at index 3


# to insert the element in the list at particular index we use insert() follows with index number
numbers.insert(2,40) # by default it will add at the end of the list
print("The entire list after adding 40 at index 2: ",numbers)


# NOTE : inseting does not mean replacing the value it only add the value in the list at particular index number
#NOTE : for replacing the value we dont have method called replace() simply we use: listname with index number = value to be replaced

numbers[0] = 100
print("The entire list after replacing 100 at index 0: ",numbers)  # at the position 0 we have replaced the value with 100 older is 10


# the length of the list
print("The length of the list: ",len(numbers))


# NOTE : defination of for-loop() :for loop is used to perform repeatative task, it works on the number of iteration returned by the iterable

print("Printing Through the for loop: ")
for n in numbers:
    print(n)


    # now in this above case we can perform arithmetic operations on the elements of the list
    # like:
        # for n in numbers:
            # print(n+1)

