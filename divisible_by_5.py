def ChkDivisible(num):

    if(num % 5 == 0):
        return True
    else:
        return False
    
No = int(input("Enter a number : "))
result = ChkDivisible(No)
print(result)
