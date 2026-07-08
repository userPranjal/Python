# Accepts a number and return number of digits in that number

def AddDigits(No1):

    Sum = 0

    while No1 > 0:
        Digit = No1 % 10
        Sum = Sum + Digit
        No1 = No1 // 10

    return Sum

Num = int(input("Enter any number : "))

Result = AddDigits(Num)
print("Addition of digits : ",Result)

