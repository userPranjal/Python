# Lambda function using filter() which accepts a list of strings and returns a list of strings having 
# length greater than 5

CheckLength = lambda String : len(String) > 5

def main():
    Size = int(input("Enter number of strings : "))

    Data = []

    for i in range(Size):
        Value = input("Enter string : ")
        Data.append(Value)

    print("Input data is : ", Data)

    FData = list(filter(CheckLength, Data))

    print("Data after FILTER : ", FData)

if __name__ == "__main__":
    main()