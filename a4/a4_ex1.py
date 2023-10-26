def split_list(lst: list, num_sublists: int):
    if num_sublists == 0:
        return lst

    sublists = [[] for i in range(num_sublists)]

    # sublist_size = int(len(lst) / num_sublists)
    # remainder = len(lst) % num_sublists
    # sublists = []
    # start = 0
    # for i in range(num_sublists):
    #     end = start + sublist_size + (1 if i < remainder else 0)
    #     sublists.append(lst[start:end])
    #     start = end

    for idx, entry in enumerate(lst):
        sublists[idx % num_sublists].append(entry)
        
    return sublists

print(split_list([0,1,2,3], 2))
print(split_list([0,1,2,3], 1))
print(split_list([0,1,2,3,4,5,6,7], 3))
print(split_list([0,1,2,3,4,5,6,7], 0))
print(split_list([0,1,2,3,4], 2))