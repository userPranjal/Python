#Display pattern    Input: 5
# * * * * * *
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

def Stars(num):
    for i in range(num,0,-1):
        for j in range(i):
            print(" * ",end=" ")
        print()

number = int(input("Enter a number: "))
Stars(number)
