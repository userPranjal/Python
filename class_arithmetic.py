class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second value : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):

        try:

            return self.Value1 / self.Value2
        
        except Exception as eobj:
            print("Exception occured : ",eobj)

Aobj1 = Arithmetic()
Aobj2 = Arithmetic()

Aobj1.Accept()
print("Addition is : ",Aobj1.Addition())
print("Multiplication is : ",Aobj1.Multiplication())
print("Substraction is : ",Aobj1.Subtraction())
print("Division is : ",Aobj1.Division())
print()

Aobj2.Accept()
print("Addition is : ",Aobj2.Addition())
print("Multiplication is : ",Aobj2.Multiplication())
print("Substraction is : ",Aobj2.Subtraction())
print("Division is : ",Aobj2.Division())