import multiprocessing
import os

def OddCount(num):
    count = 0

    for i in range(1, num + 1, 2):
        count = count + 1

    print("Process ID :", os.getpid())
    print("Input Number :", num)
    print("Odd Number Count :", count)
    print()

    return count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    result = pobj.map(OddCount, Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()