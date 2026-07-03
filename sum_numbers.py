#accepts one number and prints sum of first N natural numbers

def SumNatural(num):
    sum = 0

    for i in range(1, num + 1):
        sum = sum + i

    return sum


def main():
    no = int(input("Enter a number: "))

    result = SumNatural(no)
    print(result)


if __name__ == "__main__":
    main()