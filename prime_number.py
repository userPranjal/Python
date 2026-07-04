def Prime(num):
    if num<=1:
        return False
    
    for i in range(2,num):
        if num % 2 == 0:
            return False
        
    return True

def main():
    no = int(input("Enter a number : "))

    if Prime(no):
        print("Prime Number")

    else:
        print("Not Prime Number")

if __name__ == "__main__":
    main()