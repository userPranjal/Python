import threading

def EvenList(list1):
    EvenData = []
    sum = 0

    for i in list1:
        if i % 2 == 0:
            EvenData.append(i)
            sum = sum + i

    print("Even Numbers:", EvenData)
    print("Sum of Even numbers", sum)

def OddList(list1):
    OddData = []
    sum = 0

    for i in list1:
        if i % 2 != 0:
            OddData.append(i)
            sum = sum + i

    print("Odd Numbers", OddData)
    print("Sum of Odd numbers", sum)

def main():

    num = int(input("Enter number of elements : "))

    list1 = []

    print("Enter the elements :")

    for i in range(num):
        list1.append(int(input()))

    t1 = threading.Thread(target = EvenList, args=(list1,))
    t2 = threading.Thread(target = OddList, args=(list1,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()