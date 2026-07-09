from functools import reduce

EvenNum = lambda No : No % 2 == 0
Square = lambda No : No ** 2
Multiply = lambda No1, No2 : No1 + No2

def main():

    Num = int(input("Enter the number of elements : "))

    Data = []

    print("Enter the elements : ")

    for i in range(Num):
        Data.append(int(input()))

    print("Input Data is :",Data)

    FData = list(filter(EvenNum, Data))
    print("Data after Filter : ",FData)

    MData = list(map(Square, FData))
    print("Data after Map : ",MData)

    RData = reduce(Multiply, MData)
    print("Addition after Reduce : ",RData)

if __name__ == "__main__":
    main()
