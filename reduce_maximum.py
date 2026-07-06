# Lambda function using reduce() which accepts a list of numbers and returns the maximum element

from functools import reduce

Maximum = lambda A, B : max(A, B)

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    for i in range(Size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    print("Input data is : ", Data)

    Result = reduce(Maximum, Data)

    print("Maximum Element is : ", Result)

if __name__ == "__main__":
    main()