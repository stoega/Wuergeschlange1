import math

class Angle:
    def __init__(self, degree: float = None, radian: float = None):
        if degree is None and radian is None:
            raise ValueError("Either degree or radian must be specified.")
        
        self.degree = degree
        self.radian = radian

        if degree is not None and radian is None:
            self.radian = deg_to_rad(degree)
        elif degree is None and radian is not None:
            self.degree = rad_to_deg(radian)
        
        self.consistency()
        
    def consistency(self):
        if not math.isclose(self.degree, rad_to_deg(self.radian)):
            raise ValueError("Degree and radian are not consistent.")
    
    def __eq__(self, other):
        if isinstance(other, Angle):
            return math.isclose(self.degree, other.degree) and math.isclose(self.radian, other.radian)
        return NotImplemented
    
    def  __repr__(self):
        return f"Angle(degree={self.degree:.3f}, radian={self.radian:.3f})"
    
    def __str__(self):
        return f"{self.degree:.2f} deg = {self.radian:.2f} rad"
    
    def __add__(self, other):
        if isinstance(other, Angle):
            return Angle(self.degree + other.degree, self.radian + other.radian)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Angle):
            self.degree += other.degree
            self.radian += other.radian
            self.consistency()
            return self
        return NotImplemented
    
# Dunno
def deg_to_rad(degree):
    return degree * (math.pi / 180)

def rad_to_deg(radian):
    return radian * (180 / math.pi)

def add_all(angle: Angle, *angles: Angle):
    deg = angle.degree 
    rad = angle.radian
    
    for ang in angles:
        deg += ang.degree
        rad += ang.radian
            
        return Angle(deg, rad)
    
if __name__ == '__main__':
    a1 = Angle(degree=45)
    a2 = Angle(radian=math.pi/4)
    a3 = Angle(30, math.pi/6)
    
    print(a1)
    print(a2.__repr__())
    print(repr(a3))
    
    print(a1 == a2)
    print(a1 + a2)
    a1 += a3
    print(a1)
    
    # Hier Dunno
    sum_angle = add_all(a1, a2, a3)
    print(sum_angle)
    
    try:
        a4 = Angle()
    except ValueError as e:
        print(e)
    try:
        a5 = Angle(degree=45, radian=1)
    except ValueError as e:
        print(e)