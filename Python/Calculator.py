class Calculator():
    def __init__(self):
        self.n = []
        self.operator = None
        
    def One(self):
        self.n.append(1)
        if self.operator != None:
            self.Operate()
        return self

    def Plus(self):
        self.operator = "+"
        return self
    
    def Equals(self):
        return self.n

    def Operate(self):
        if self.operator == "+":
            self.n = sum(self.n)
            self.operator = None
calculator = Calculator()
print(calculator.One().Plus().One().Equals() == 2) 
