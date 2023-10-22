def odd_doubler(lst):
    # Create an empty list to store the doubled values
    doubled_list = []
    
    # Iterate through the input list
    for num in lst:
        if num % 2 == 1:  # Check if the number is odd
            doubled_list.append(num * 2)  # Double the odd number and add it to the new list
        else:
            doubled_list.append(num)  # Add even numbers unchanged
    
    return doubled_list

# Example usage:
input_list = [1, 2, 3, 4, 5, 6]
result = odd_doubler(input_list)
print(result)  # Output: [2, 2, 6, 4, 10, 6]
