import multiprocessing
import os

def EvenSum(num):
    Sum = 0

    for i in range(2, num + 1, 2):
        Sum = Sum + i

    print("Process ID :", os.getpid())
    print("Input Number :",num)
    print("Sum of Even Numbers :", Sum)
    print()

    return Sum


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    result = pobj.map(EvenSum, Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()