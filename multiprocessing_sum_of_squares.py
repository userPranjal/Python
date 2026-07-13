import multiprocessing

def SquaresSum(n):
    Sum = 0
    for i in range(1, n + 1):
        Sum = Sum + i * i
    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SquaresSum, Data)

    pobj.close()
    pobj.join()

    print("Input : ",Data)
    print("Sum of Squares :",Result)

if __name__ == "__main__":
    main()