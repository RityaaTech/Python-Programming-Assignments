class Arithmetic :

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("ENTER THE NUMBER : "))
        self.Value2 = int(input("ENTER THE NUMBER : "))

    def Addition(self):
        self.Addition = self.Value1 + self.Value2
        return self.Addition

    def Subtraction(self):
        self.Subtraction = self.Value1 - self.Value2
        return self.Subtraction

    def Multiplication(self):
        self.Multiplication = self.Value1 * self.Value2
        return self.Multiplication

    def Division(self):
        self.Division = self.Value1 / self.Value2
        return self.Division

Obj1 = Arithmetic()
Obj1.Accept()
print(Obj1.Addition())
print(Obj1.Subtraction())
print(Obj1.Multiplication())
print(Obj1.Division())
