# Lambda function that accepts two numbers and returns multiplication

Multiply = lambda No1, No2 : (No1*No2)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number :"))

    Ret = Multiply(Value1,Value2)

    print("Multiplacation is :", Ret)

if __name__ == "__main__":
    main()