import MarvellousNum


def ListPrime(numbers):
    sum = 0

    for num in numbers:
        if MarvellousNum.ChkPrime(num):
            sum = sum + num

    return sum


def main():
    n = int(input("Enter the number of elements: "))

    numbers = []

    print("Enter the elements : ")

    for i in range(n):
        num = int(input())
        numbers.append(num)

    result = ListPrime(numbers)

    print("Sum of prime numbers:", result)


if __name__ == "__main__":
    main()