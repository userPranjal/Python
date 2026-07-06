# Lambda function using filter() which accpets a list of numbers and returns a list of numbers 
# divisible by both 3 and 5

CheckDivisible = lambda No : (No % 3 == 0) and (No % 5 == 0)

def main():
    Size = int(input("Enter total number of elements : "))

    Data = []

    for i in range(Size):
        Value = int(input("Enter element : "))
        Data.append(Value)

    print("Input data is : ", Data)

    FData = list(filter(CheckDivisible, Data))

    print("Data after FILTER : ", FData)

if __name__ == "__main__":
    main()