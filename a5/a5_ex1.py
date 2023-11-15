def sub_summarize(nested: list, sub_sums: list) -> int:
    # Base case: if the input is not a list, return its value
    if not isinstance(nested, list):
        return nested
    
    # Initialize the sum for the current level
    current_sum = 0
    
    # Iterate through the elements in the current level
    for element in nested:
        # Recursively call sub_summarize for each element
        current_sum += sub_summarize(element, sub_sums)
    
    # Append the sum for the current level to sub_sums
    sub_sums.append(current_sum)
    
    # Return the sum for the current level
    return current_sum

nested = [1, 2, 3, [4, [5, 6], 7], 8, [9, 10]]
sub_sums = []
sum = sub_summarize(nested, sub_sums)
print(sub_sums)
print(sum)



