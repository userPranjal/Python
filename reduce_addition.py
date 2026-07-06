# Lambda function using reduce() which accepts a list of numbers and returns the addition of all elements

from functools import reduce

Addition = lambda A, B : A + B

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    for i in range(Size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    print("Input data is : ", Data)

    Result = reduce(Addition, Data)

    print("Addition of all elements : ", Result)

if __name__ == "__main__":
    main()