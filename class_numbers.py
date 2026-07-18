class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if(self.Value < 1):
            return False
        
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True
    
    def ChkPerfect(self):
        sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i

        return sum == self.Value

    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i

        return sum
    
Nobj1 = Numbers(int(input("Enter First Number: ")))
print("Prime:", Nobj1.ChkPrime())
print("Perfect:", Nobj1.ChkPerfect())
Nobj1.Factors()
print("Sum of Factors:", Nobj1.SumFactors())

print()

Nobj2 = Numbers(int(input("Enter First Number: ")))
print("Prime:", Nobj2.ChkPrime())
print("Perfect:", Nobj2.ChkPerfect())
Nobj2.Factors()
print("Sum of Factors:", Nobj2.SumFactors())