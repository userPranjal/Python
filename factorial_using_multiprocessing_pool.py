# Factorial of multiple numbers using multiprocessing.pool 
# Data=[10,15,20,25]

import multiprocessing
import os

def Factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print("Process ID :", os.getpid())
    print("Input Number :", num)
    print("Factorial  :", fact)
    print()

    return fact

def main():
    Data = [10, 15, 20, 25]

    pobj = multiprocessing.Pool()

    result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()