# Display Star Pattern 
# Input : 5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def Stars(num):
    for i in range(num):
        for j in range(num):
            print(" * ",end=" ")
        print()

number = int(input("Enter a number: "))
Stars(number)
