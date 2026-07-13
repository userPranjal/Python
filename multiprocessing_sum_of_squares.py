from multiprocessing import Pool

def SquaresSum(n):
    Sum = 0
    for i in range(1, n + 1):
        Sum = Sum + i * i
    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pool = Pool()

    result = pool.map(SquaresSum, Data)

    pool.close()
    pool.join()

    print("Input : ",Data)
    print("Sum of Squares :",result)

if __name__ == "__main__":
    main()