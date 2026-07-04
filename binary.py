#Accepts one number and prints binary equivalent

def DecimalToBinary(num):
    binary = ""

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    return binary


def main():
    no = int(input("Enter a number: "))

    result = DecimalToBinary(no)
    print("Binary equivalent is:", result)


if __name__ == "__main__":
    main()