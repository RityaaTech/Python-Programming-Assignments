class Circle:
    Pi = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("ENTER THE RADIUS OF THE CIRCLE : "))
        

    def CalulateArea(self):
        self.Area = 3.14 * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.Pi * self.Radius
        
    def Display(self):
        print(f"RADIUS : {self.Radius}")
        print(f"CIRCUMFERENCE : {self.Circumference}")
        print(f"AREA : {self.Area}")


Obj1 = Circle() 
Obj1.Accept() 
Obj1.CalulateArea()
Obj1.CalculateCircumference()
Obj1.Display()




