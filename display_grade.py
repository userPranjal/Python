#Accepts marks and display grade

def Grade(no):
    if(no >= 75):
        print("Distinction")
    elif(no >= 60):
        print("First Class")
    elif(no >= 50):
        print("Second Class")
    else:
        print("Fail")
    

def main():
    marks = float(input("Enter your marks : "))

    Grade(marks)

if __name__ == "__main__":
    main()