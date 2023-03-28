class Calc1:
    def add(self,a,b):
        return a + b
class Calc2:
    def subtract(self,a,b):
        return a - b

class Calc3:
    def multiply(self,a,b):
        return a * b

class Calculation(Calc3,Calc2,Calc1):
    def divide(self,a,b):
        return a/b

c = Calculation()
print(c.add(5,6))
print(c.divide(30,3))



