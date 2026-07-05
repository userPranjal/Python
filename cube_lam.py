#Lambda function to calculate the cube of a number

Cube = lambda x: x * x * x

def main():
    num = int(input("Enter a number: "))

    Ret = Cube(num)
    print("Cube:", Ret)

if __name__ == "__main__":
    main()