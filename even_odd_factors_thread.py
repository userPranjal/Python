import threading

def EvenFactor(num):
    EvenData = []
    sum = 0

    for i in range(2,num+1):
        if(i % 2 == 0) and (num % i == 0):
            EvenData.append(i)
            sum = sum + i

    print("Even Factors:", EvenData)
    print("Sum of Even Factors:", sum)

def OddFactor(num):
    OddData = []
    sum = 0

    for i in range(1,num+1):
        if(i % 2 != 0) and (num % i == 0):
            OddData.append(i)
            sum = sum + i

    print("Odd Factors:", OddData)
    print("Sum of Odd Factors:", sum)

def main():
    even_no = int(input("Enter number for EvenFactor: "))
    odd_no = int(input("Enter number for OddFactor: "))

    t1 = threading.Thread(target = EvenFactor, args=(even_no,))
    t2 = threading.Thread(target = OddFactor, args=(odd_no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()