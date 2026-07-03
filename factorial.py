def Factorial(num):
    fact = 1

    for i in range(1,num + 1):
        fact = fact * i

    return fact


def main():
    no = int(input("Enter a number: "))

    result = Factorial(no)
    print("Factorial of", no, "is:", result)


if __name__ == "__main__":
    main()