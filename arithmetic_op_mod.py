# Program which call the functions from ArithemeticModule module

from ArithmeticModule import *

def main():
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))

    Ret = Add(Value1, Value2)
    print("Addition is : ",Ret)

    Ret = Sub(Value1, Value2)
    print("Subtraction is : ",Ret)

    Ret = Mult(Value1, Value2)
    print("Multiplication is : ",Ret)

    Ret = Div(Value1, Value2)
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()