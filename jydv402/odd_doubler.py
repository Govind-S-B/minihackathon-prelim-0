def odd_doubler(input):
    """
    task : complete the function odd_doubler which doubles the value of all the odd numbers in the list it receives and returns it
    - accepts a list of integers
    - returns a list of integers

    example :
    input -> [1, 2, 3, 4, 5]
    output -> [2, 2, 6, 4, 10]
    """

    output = []
    
    for digit in input:
        if digit % 2 != 0:
            output.append(digit * 2)
        else:
            output.append(digit)

    return output