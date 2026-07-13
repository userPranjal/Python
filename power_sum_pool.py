import multiprocessing
import time

def PowerSum(n):
    Sum = 0

    for i in range(1, n + 1):
        Sum = Sum + (i ** 5)

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    result = pobj.map(PowerSum, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result:")
    for i in range(len(Data)):
        print("Input Number =", Data[i])
        print("Sum =", result[i])
        print()

    print("Total Execution Time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()
