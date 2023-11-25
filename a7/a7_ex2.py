import math

class Rotate:
    matrix: list
    degree: float
    inplace: bool
    
    def __init__(self, matrix: list, degree: float, inplace = False):
        self.matrix = matrix
        self.degree = degree
        self.inplace = inplace
    
    def rotation(self):
        from a7_ex1 import Radian  # Assuming Radian class is available

        radian = Radian(self.degree).rad()
        cos_val = round(math.cos(radian), 2)
        sin_val = round(math.sin(radian), 2)

        n = len(self.matrix)
        rotated_matrix = [[0] * n for _ in range(n)]

        for i in range(n):  # rows
            for j in range(n):  # cols
                if self.degree == 90:
                    if self.inplace:
                        self.matrix[i][j] = self.matrix[n - j - 1][i]
                    else:
                        rotated_matrix[i][j] = self.matrix[n - j - 1][i]
                elif self.degree == -90:
                    if self.inplace:
                        self.matrix[i][j] = self.matrix[j][n - i - 1]
                    else:
                        rotated_matrix[i][j] = self.matrix[j][n - i - 1]
                elif self.degree == 180:
                    if self.inplace:
                        self.matrix[i][j] = self.matrix[n - i - 1][n - j - 1]
                    else:
                        rotated_matrix[i][j] = self.matrix[n - i - 1][n - j - 1]

        return self.matrix if self.inplace else rotated_matrix
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
c1 = Rotate(matrix,90)
c11= c1.rotation()
print(c11)
print(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
c2 = Rotate(matrix,-90, True)
c22= c2.rotation()
print(c22)
print(matrix)

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
c3 = Rotate(matrix,180)
c33 = c3.rotation()
print(c33)