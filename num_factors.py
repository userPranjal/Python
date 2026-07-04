#Accepts one number and prints its factors

def Factors(num):
    for i in range(1,num+1):
        if(num % i == 0):
            print(i)

def main():
    value = int(input("Enter a number : "))

    Factors(value)

if __name__ == "__main__":
    main()