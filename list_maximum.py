# Displaying maximum number from list

def Maximum(numbers):
    for num in numbers:
       num = max(numbers)

    return num

def main():
    no = int(input("Enter number of elements :"))

    numbers = []

    print("Enter the elements : ")

    for i in range(no):
        num = int(input())
        numbers.append(num)

    result = Maximum(numbers)

    print("List :",numbers)
    print("Maximum number is :",result)

if __name__ == "__main__":
    main()