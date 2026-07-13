import multiprocessing
import os

def Factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i

    print("Process ID:", os.getpid())
    return result

def main():
    Data = [10,15,20,25]

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    print("Input Number : ",Data)
    print("Factorial :",Result)

if __name__ == "__main__":
    main()

  