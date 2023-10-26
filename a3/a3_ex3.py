user_input = input("Enter comma-separated elements: ")
entries = user_input.split(",")
hash_dict = {}

for entry in entries:
    hash_value = 0
    for char in entry:
        hash_value += ord(char)
    
    if entry in hash_dict:
        assert hash_dict[entry] == hash_value
    else:
        hash_dict[entry] = hash_value
    
for key, value in hash_dict.items():
    print(f"{key} -> {value}")