#Lambda function to calculate the square of a number

Square = lambda x: x * x

def main():
    num = int(input("Enter a number: "))

    Ret = Square(num)
    print("Square:", Ret)

if __name__ == "__main__":
    main()