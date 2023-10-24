def odd_doubler(arr):
    """
    task : complete the function odd_doubler which doubles the value of all the odd numbers in the list it receives and returns it
    - accepts a list of integers
    - returns a list of integers

    example :
    input -> [1, 2, 3, 4, 5]
    output -> [2, 2, 6, 4, 10]
    """

    if len(arr) == 0:
        return []

    for i in range (0, len(arr)):
        if arr[i] % 2 != 0:
            arr[i] = arr[i] * 2
    
    return arr
    
    pass
