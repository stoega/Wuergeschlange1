start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

nEven = 0
sumOdd = 0
index = 0

for num in range(start, stop, step):
    if(index < 5):
        print(f"Number in iteration {index} = {num}")
    if(num % 2 == 0):
        nEven += 1
    else:
        sumOdd += num
    index += 1
print(f"Even number count = {nEven}")
print(f"Sum of odd numbers = {sumOdd}")