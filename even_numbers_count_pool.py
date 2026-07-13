import multiprocessing
import os

def EvenCount(num):
    count = 0

    for i in range(2, num + 1, 2):
        count = count + 1

    print("Process ID :", os.getpid())
    print("Input Number :", num)
    print("Even Number Count :", count)
    print()

    return count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    result = pobj.map(EvenCount, Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()