from functools import reduce

Filter1 = lambda No : (No >= 70) and (No <= 90) 
Increament = lambda No : No + 10
Multiply = lambda No1, No2 : No1 * No2

def main():

    Num = int(input("Enter the number of elements : "))

    Data = []

    print("Enter the elements : ")

    for i in range(Num):
        Data.append(int(input()))

    print("Input Data is :",Data)

    FData = list(filter(Filter1, Data))
    print("Data after Filter : ",FData)

    MData = list(map(Increament, FData))
    print("Data after Map : ",MData)

    RData = reduce(Multiply, MData)
    print("Product after Reduce : ",RData)

if __name__ == "__main__":
    main()
