def Area(r):
    PI = 3.14
    CircleArea = PI * r * r
    print("Area of Circle : ",CircleArea)

def main():

    radius = float(input("Enter the radius : "))

    Area(radius)

if __name__ == "__main__":
    main()