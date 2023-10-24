size = int(input("Enter number of lines: "))

if(size < 3):
    print("Invalid number of lines")
    exit(0)

print("-"*size)
for row in range(2, size):
    print("|" + " "*(size - 2) + "|")
print("-"*size)
