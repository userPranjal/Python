from functools import reduce

def ChkPrime(num):
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True
    
def Multiply(num):
    return num * 2

def Maximum(No1, No2):
    return max(No1, No2)

def main():

    Num = int(input("Enter the number of elements : "))

    Data = []

    print("Enter the elements : ")

    for i in range(Num):
        Data.append(int(input()))

    print("Input Data is :",Data)

    FData = list(filter(ChkPrime, Data))
    print("Data after Filter : ",FData)

    MData = list(map(Multiply, FData))
    print("Data after Map : ",MData)

    RData = reduce(Maximum, MData)
    print("Maximum number after Reduce : ",RData)

if __name__ == "__main__":
    main()
