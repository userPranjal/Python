# Lambda function using map() to return the square of each number in a list

Square = lambda No : No * No

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    for i in range(Size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    print("Input data is : ", Data)

    MData = list(map(Square, Data))

    print("Data after MAP : ", MData)

if __name__ == "__main__":
    main()