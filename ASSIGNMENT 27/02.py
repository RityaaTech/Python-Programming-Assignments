class BankAccount:

    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"ACCOUNT FOLDER NAME : {self.Name}")
        print(f"CURRENT BALANCE : {self.Amount}")

    def Deposit(self):
        self.add_amount = int(input("ENTER THE AMOUNT : "))
        self.Deposit = self.add_amount + self.Amount

    def Withdraw(self):
        self.Withdraw_amount = int(input("ENTER THE AMOUNT : "))
        self.Withdraw = self.Deposit - self.Withdraw_amount

    def Show(self):
        print(f"DEPOSIT AMOUNT : $ {self.Deposit}")
        print(f"WITHDRAW AMOUNT : $ {self.Withdraw}")

    def Calculate_Interest(self):
        self.Calculate_Interest = (self.Withdraw*BankAccount.ROI) / 100
        print(self.Calculate_Interest)

Obj1 = BankAccount("Ritesh Saptale",75000)
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
Obj1.Show()
Obj1.Calculate_Interest()