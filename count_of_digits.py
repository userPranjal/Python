#Accepts a number and prints count of digits in that number

def CountNo(No1):

    count = 0

    while No1 > 0:
        count = count + 1
        No1 = No1 // 10

    return count

def main():
    num = int(input("Enter any number : "))

    result = CountNo(num)
    print("Count of digits : ",result)

if __name__ == "__main__":
    main()