# Lambda function using reduce() which accepts list of numbers and returns the product of all elements

from functools import reduce

Product = lambda No1,No2 : No1 * No2

Increment = lambda No : No+1

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    for i in range(Size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    print("Input data is : ", Data)

    Result = reduce(Product, Data)

    print("Product is : ", Result)

if __name__ == "__main__":
    main()