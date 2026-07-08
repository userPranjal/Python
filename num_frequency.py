# Accept N numbers from user and storing it as list. Accept one another number from user and return
# frequency of that number from list

def Frequency(numbers,checknum):
    count = 0
    for num in numbers:
        if num == checknum:
            count = count + 1
    return count

def main():
    no = int(input("Enter number of elements :"))

    numbers = []

    print("Enter the elements : ")

    for i in range(no):
        num = int(input())
        numbers.append(num)   

    checknum = int(input("Enter the number to check it's frequency : "))

    result = Frequency(numbers,checknum)

    print("List :",numbers)
    print("Frequency of", checknum, "is:", result)

if __name__ == "__main__":
    main()