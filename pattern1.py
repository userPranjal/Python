# Display pattern   Input = 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def Stars(num):
    for i in range(num):
        for j in range(1,num+1):
            print(j,end=" ")
        print()

number = int(input("Enter a number: "))
Stars(number)
