#Accepts a number and prints the reverse of that number

def ReverseNumber(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

def main():
    no = int(input("Enter a number: "))

    result = ReverseNumber(no)
    print("Reverse Number:", result)

if __name__ == "__main__":
    main()