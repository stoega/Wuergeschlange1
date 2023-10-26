elements = []
# Sets are unordered collections of unique elements
uniqe_elements = set()

while True:
    user_input = input("Enter element or 'x' when done: ")
    if user_input.lower() == 'x':
        break
    elements.append(user_input)
    uniqe_elements.add(user_input)
    
#sort uniqe elements
uniqe_elements = sorted(uniqe_elements)
    
print(f"all: {elements}")
print(f"unique (sorted): {uniqe_elements}")
