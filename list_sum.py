# Addition of elements from the list

def AddSum(numbers):
    sum = 0

    for num in numbers:
        sum = sum + num

    return sum

def main():
    no = int(input("Enter number of elements : "))

    numbers = []

    print("Enter the elements : ")

    for i in range(no):
        num = int(input())
        numbers.append(num)

    result = AddSum(numbers)

    print("List :",numbers)
    print("Sum of all elements : ",result)

if __name__ == "__main__":
    main()