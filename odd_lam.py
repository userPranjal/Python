# Lambda function that accepts one number and returns True if number is odd otherwise False

CheckOdd = lambda No : (No % 2 != 0)

def main():
    Value = int(input("Enter number : "))

    Ret = CheckOdd(Value)      

    print(Ret)

if __name__ == "__main__":
    main()