Multiplication = lambda NO1, NO2 : NO1 * NO2

def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number : "))

    Ret = Multiplication(Num1, Num2)

    print("Multiplication is :",Ret)

if __name__ == "__main__":
    main()