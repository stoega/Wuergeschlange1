start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

n_even = 0
sum_odd = 0
index = 0

for num in range(start, stop, step):
    if(index < 5):
        print(f"Number in iteration {index} = {num}")
    if(num % 2 == 0):
        n_even += 1
    else:
        sum_odd += num
    index += 1
print(f"Even number count = {n_even}")
print(f"Sum of odd numbers = {sum_odd}")