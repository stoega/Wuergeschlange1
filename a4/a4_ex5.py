def sort_(elements: list, ascending: bool = True):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and ((elements[j] > key) if ascending else (elements[j] < key)):
            #swap elements
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
        

# some_list = [1, 3, 0, 4, 5]
# sort_(some_list)
# print(some_list)
# sort_(some_list, ascending=False)
# print(some_list)