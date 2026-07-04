def Area(no1,no2):
    recarea = no1 * no2
    print("Area of Rectangle : ",recarea)

def main():
    length = int(input("Enter the length : "))
    width = int(input("Enter the width : "))

    Area(length,width)

if __name__ == "__main__":
    main()