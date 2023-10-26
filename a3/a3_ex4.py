user_input = input("Enter comma-separated elements: ")
parts = user_input.split(',')

integers = []
counts = {}
rest = []

for part in parts:
    if part.isdecimal():
        integers.append(int(part))
        
        if part in counts:
            counts[part] += 1
        else:
            counts[part] = 1   
    else:
        rest.append(part)

print(f"integers: {integers}")
print(f"counts: {counts}")
print(f"rest: {rest}")