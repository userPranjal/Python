# Lambda function using filter() to return the odd number of each number in a list

CheckOdd = lambda No : (No % 2 != 0)

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    for i in range(Size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    print("Input data is : ", Data)

    FData = list(filter(CheckOdd, Data))

    print("Data after FILTER : ", FData)

if __name__ == "__main__":
    main()