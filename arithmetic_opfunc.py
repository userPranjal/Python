#Accepts two numbers and prints addition, subtraction, multiplication, divide

def Arithmetic(value1,value2):

    print("Addition = ",value1 + value2)
    print("Subtraction = ",value1 - value2)
    print("Multiplication = ",value1 * value2)
    print("Division = ",value1 / value2)

def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number: "))

    Arithmetic(num1,num2)

if __name__ == "__main__":
    main()