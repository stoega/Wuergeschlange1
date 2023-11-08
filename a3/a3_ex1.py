rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))

matrix = [[0 for col in range(cols)] for row in range(rows)]

for i in range(min(rows, cols)):
    matrix[i][i] = 1
        
print(" " * 3 + " ".join(str(col) for col in range(cols)))
print(" " * 2 + "-" * cols * 2)
for row in range(rows):
    print(f"{row}| " + " ".join(str(col) for col in matrix[row]))
    