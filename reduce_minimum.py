# Lambda function using reduce() which accepts a list of numbers and returns the minimum element

from functools import reduce

Minimum = lambda A, B : min(A, B)

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    for i in range(Size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    print("Input data is : ", Data)

    Result = reduce(Minimum, Data)

    print("Minimum Element is : ", Result)

if __name__ == "__main__":
    main()