def ChkGreater(value1, value2):
    if(value1 > value2):
        print(value1, "is greater ")
    else:
        print(value2, "is greater ")   

def main():
    no1 = int(input("Enter first numbers : "))
    no2 = int(input("Enter second numbers : "))

    ChkGreater(no1, no2)

if __name__ == "__main__":
    main()