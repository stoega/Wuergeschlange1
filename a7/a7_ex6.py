from a7_ex4 import Minkowski

class Euclidean(Minkowski):
    def __init__(self, x:int, vect1:list, vect2:list):
        super().__init__(x, vect1, vect2)
    
    def to_string(self) -> str:
        return f"Euclidean: x={self.x}, vector_1={self.vect1}, vector_2={self.vect2}"
    
    def dist(self) -> float:
        distance = 0
        for i in range(len(self.vect1)):
            distance += (self.vect1[i] - self.vect2[i])**2
        return round(distance**(1/2), 4)