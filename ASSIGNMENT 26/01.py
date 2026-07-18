class Demo:
    Value = 5

    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    def Fun(self):
        print(self.No1)
        print(self.No2)

    def Gun(self):
        print(self.No1)
        print(self.No2)

Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()

Obj1.Gun()
Obj2.Gun()