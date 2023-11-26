import math

class Radian:
    def __init__(self, degree: float):
        self.degree = degree
    
    def rad(self) -> float:
        return self.degree * math.pi/180
    
    def print(self):
        print(f"The degree is {self.degree:.2f} and the radian is {self.rad():.2f}")
        
c = Radian(90)
print(c.rad())
c.print()