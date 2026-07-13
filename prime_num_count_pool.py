import multiprocessing

def Prime(no):
    count = 0

    for num in range(2, no + 1):
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            count = count + 1

    return count

def main():
    numbers = []

    size = int(input("Enter how many numbers: "))

    for i in range(size):
        no = int(input("Enter number: "))
        numbers.append(no)

    pobj = multiprocessing.Pool()

    result = pobj.map(Prime, numbers)

    pobj.close()
    pobj.join()

    print("Result:")
    for i in range(len(numbers)):
        print("Total prime numbers between 1 and", numbers[i], "=", result[i])

if __name__ == "__main__":
    main()