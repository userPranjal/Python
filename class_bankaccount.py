class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name : ",self.Name)
        print("Current Balance : ",self.Amount)

    def Deposit(self):
        deposit = float(input("Enter an Amount to Deposit : "))
        self.Amount = self.Amount + deposit
        print("Amount Deposited Successfully")
        print("Your Current Amount is : ",self.Amount)
        print()

    def Withdraw(self):
        withdraw = float(input("Enter an Amount To Withdraw : "))

        if(withdraw < self.Amount):
            self.Amount = self.Amount - withdraw
            print("Withdrawal Successfull")

        else:
            print("Insufficient Balance ")

        print("Your Current Amount is : ",self.Amount)

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) /100
        print("Interest : ",interest)

Bobj1 = BankAccount("Pranjal", 7000)
Bobj1.Display()
Bobj1.Deposit()
Bobj1.Withdraw()
Bobj1.CalculateInterest()

print()
print()

Bobj2 = BankAccount("Sanika", 988.80)
Bobj2.Display()
Bobj2.Deposit()
Bobj2.Withdraw()
Bobj2.CalculateInterest()