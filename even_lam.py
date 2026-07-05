# Lambda function that accepts one number and returns True if number is even otherwise False

CheckEven = lambda No : (No % 2 == 0)

def main():
    Value = int(input("Enter number : "))

    Ret = CheckEven(Value)      

    print(Ret)

if __name__ == "__main__":
    main()