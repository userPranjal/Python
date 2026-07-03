#Accepts a number and prints all odd number till that number

def Even(num):
    for i in range(1, num + 1):
        if i % 2 == 1:
            print(i)


def main():
    no = int(input("Enter a number: "))
    Even(no)


if __name__ == "__main__":
    main()