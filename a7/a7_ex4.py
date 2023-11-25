from a7_ex3 import Distance

class Minkowski(Distance):
    vect1: list
    vect2: list
    
    def __init__(self, x: int, vect1: list, vect2: list):
        super().__init__(x)
        self.x = x
        self.vect1 = vect1
        self.vect2 = vect2
    
    def to_string(self) -> str:
        return f"Minkowski: the number of vectors ={self.x}, vector_1={self.vect1}, vector_2={self.vect2}"
    
    def dist(self) -> float:
        distance = 0
        for i in range(len(self.vect1)):
            distance += abs(self.vect1[i] - self.vect2[i]) ** self.x
        
        return round(distance ** (1 / self.x), 4)