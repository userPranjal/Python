import threading

def Small(text):
    count = 0

    for ch in text:
        if ch.islower():
            count = count + 1

    print("TID of Small Thread is :",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase Characters :", count)
    print()


def Capital(text):
    count = 0

    for ch in text:
        if ch.isupper():
            count = count + 1
    
    print("TID of Capital Thread is :",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase Characters :", count)
    print()


def Digits(text):
    count = 0

    for ch in text:
        if ch.isdigit():
            count = count + 1

    print("TID of Digits Thread is :",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", count)


def main():
    string = input("Enter a string :")

    t1 = threading.Thread(target=Small, args=(string,), name= "Small")
    t2 = threading.Thread(target=Capital, args=(string,), name= "Capital")
    t3 = threading.Thread(target=Digits, args=(string,), name= "Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()