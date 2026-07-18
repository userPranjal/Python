class Circle:
    
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the Radius of the Circle : "))

    def CalculateArea(self):
        self.Area = self.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print("Radius : ",self.Radius)
        print("Area : ",self.Area)
        print("Circumference : ",self.Circumference)

Cobj1 = Circle()
Cobj2 = Circle()

Cobj1.Accept()
Cobj1.CalculateArea()
Cobj1.CalculateCircumference()
Cobj1.Display()

Cobj2.Accept()
Cobj2.CalculateArea()
Cobj2.CalculateCircumference()
Cobj2.Display()