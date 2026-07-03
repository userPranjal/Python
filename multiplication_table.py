#Accepts a number and prints multiplication table of that number

def Multiply(no1):
    
    for i in range(1,11,1):
        result = no1 * i
    
        print(result)

def main():
    num = int(input("Enter the number : "))

    Multiply(num)

if __name__ == "__main__":
    main()