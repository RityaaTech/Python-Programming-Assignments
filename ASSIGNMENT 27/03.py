class Numbers :

    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1 :
            return False
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        s = 0
        for i in range(1,self.Value):
            if (self.Value % i == 0):
                s = s + i
        return s == self.Value

    def Factors(self):
        print(f"Factors of {self.Value} are : ")
        for i in range(1,self.Value+1):
            if (self.Value % i == 0):
                print(i,end = " ")
        print()

    def SumFactors(self):
        s = 0
        for i in range(1,self.Value+1):
            if (self.Value % i == 0):
                s = s + i
        return s 


Obj1 = Numbers(7)
print(Obj1.ChkPrime())
print(Obj1.ChkPerfect())
print(Obj1.Factors())
print(Obj1.SumFactors())
        