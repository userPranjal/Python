# Displaying minimum number from list

def Minimum(numbers):
    for num in numbers:
       num = min(numbers)

    return num

def main():
    no = int(input("Enter number of elements :"))

    numbers = []

    print("Enter the elements : ")

    for i in range(no):
        num = int(input())
        numbers.append(num)

    result = Minimum(numbers)

    print("List :",numbers)
    print("Minimum number is :",result)

if __name__ == "__main__":
    main()