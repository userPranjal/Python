import threading

def Thread1(num):
    for i in range(1,51):
        print(i)


def Thread2(num):
    for i in range(51,0,-1):
        print(i)

def main():

    number = print("Displaying numbers from 1 to 50 :")
    Thread1(number)
    print()
    
    reverse = print("Displaying numbers from 50 to 1 :")
    Thread2(reverse)

    t1 = threading.Thread(target=number)
    t2 = threading.Thread(target=reverse)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()