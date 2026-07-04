#Accepts one number and prints that many numbers starting from 1

def Number(num):
    for i in range(1,num+1):
        print(i)

def main():
    no = int(input("Enter the number :"))

    Number(no)

if __name__ == "__main__":
    main()