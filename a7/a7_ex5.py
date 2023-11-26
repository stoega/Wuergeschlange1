from a7_ex3 import Distance

class Manhattan(Distance):
    def __init__(self, x: int, vect1: list, vect2: list):
        super().__init__(x)
        self.vect1 = vect1
        self.vect2 = vect2
    
    def to_string(self):
        return f"Manhattan: the number of vectors ={self.x}, vector_1={self.vect1}, vector_2={self.vect2}"
    
    def dist(self):
        distance = 0
        for i in range(len(self.vect1)):
            distance += abs(self.vect1[i] - self.vect2[i])
        return round(distance, 4)

