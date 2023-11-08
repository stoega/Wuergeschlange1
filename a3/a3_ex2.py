elements = []

user_input = ""
while True:
    user_input = input("Enter element or 'x' when done: ")
    if user_input.lower() == 'x':
        break
    elements.append(user_input)
    
#sort uniqe elements
uniqe_elements = set(elements)
uniqe_elements = sorted(uniqe_elements)
    
print(f"all: {elements}")
print(f"unique (sorted): {uniqe_elements}")