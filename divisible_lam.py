# Lambda function that accepts one number and returns True if divisible by 5

Divisible = lambda No : (No % 5 == 0)

def main():
    Value = int(input("Enter number : "))

    Ret = Divisible(Value)      

    print(Ret)

if __name__ == "__main__":
    main()