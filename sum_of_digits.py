#Accepts a number and prints sum of digits

def Sum(num):
    sum = 0 

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    return sum

def main():
    no = int(input("Enter the number : "))

    result = Sum(no)
    print(result)

if __name__ == "__main__":
    main()