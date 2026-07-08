def PrimeNum(num):
    for i in range(2,num):
        if num % 2 == 0:
            return False
        
    return True

value  = int(input("Enter a number : "))
if PrimeNum(value):
    print("Prime Number")

else:
    print("Not Prime Number")

PrimeNum(value)