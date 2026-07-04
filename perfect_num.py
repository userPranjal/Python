#Accepts one number and checks whether it is perfect number or not

def CheckPerfect(num):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        return True
    else:
        return False

def main():
    no = int(input("Enter a number: "))

    if CheckPerfect(no):
        print("Perfect Number")
    else:
        print("Not Perfect Number")

if __name__ == "__main__":
    main()