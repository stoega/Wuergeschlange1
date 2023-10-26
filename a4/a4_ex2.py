def clip(*values, min_ = 0, max_ = 1):
    clipped_list = []
    for value in values:
        if value < min_:
            clipped_list.append(min_)
        elif value > max_:
            clipped_list.append(max_)
        else:
            clipped_list.append(value)
    return clipped_list


print(clip())
print(clip(1, 2, 0.1, 0))
print(clip(-1, 0.5))
print(clip(-1, 0.5, min_=-2))
print(clip(-1, 0.5, max_=0.3))
print(clip(-1, 0.5, min_=2, max_=3))
