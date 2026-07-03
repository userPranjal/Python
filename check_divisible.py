def ChkDivisible(value):
    if(value % 3 == 0 and value % 5 == 0):
        print("Divisile by 3 and 5")
    else:
        print("Not divisible by 3 and 5")
        
def main():
    num = int(input("Enter the number : "))

    ChkDivisible(num)

if __name__ == "__main__":
    main()