#Accepts a number and prints all even number till that number

def Even(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)


def main():
    no = int(input("Enter a number: "))
    Even(no)


if __name__ == "__main__":
    main()