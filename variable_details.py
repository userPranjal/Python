from sys import getsizeof

print("Enter the number: ")
no = int(input())

print("Value of no is : ",no)
print("ID of no is : ",id(no))
print("Type of no is : ",type(no))
print("Size of variable : ",getsizeof(no))