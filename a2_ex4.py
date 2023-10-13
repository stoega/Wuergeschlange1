import sys
size = int(input("Enter number of lines: "))

if(size < 3):
    print("Invalid number of lines")
    sys.exit()

print("-"*size)
for row in range(2, size):
    print("|" + " "*(size - 2) + "|")
print("-"*size)
