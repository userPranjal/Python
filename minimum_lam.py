# Lambda function that accepts two numbers and returns minimum number

Minimum = lambda No1, No2 : min(No1, No2)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Minimum(Value1, Value2)

    print("Minimum number is :", Ret)

if __name__ == "__main__":
    main()