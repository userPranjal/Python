#Accepts a number annd check whether it is palindrome or not

def CheckPalindrome(num):
    no1 = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if no1 == reverse:
        return True
    else:
        return False

def main():
    no = int(input("Enter a number: "))

    if CheckPalindrome(no):
        print("Palindrome number")
    else:
        print("Not Palindrome number")

if __name__ == "__main__":
    main()