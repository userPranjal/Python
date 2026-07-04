#Accepts a number and prints that many number in reverse order
#Input = 5
#Output = 5 4 3 2 1

def Reverse(num):
    for i in range(num,0,-1):
        print(i)

def main():
    no = int(input("Enter a number : "))

    Reverse(no)

if __name__ == "__main__":
    main()