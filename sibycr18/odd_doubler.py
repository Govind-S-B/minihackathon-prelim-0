def odd_doubler(integer_list):
    """
    task : complete the function odd_doubler which doubles the value of all the odd numbers in the list it receives and returns it
    - accepts a list of integers
    - returns a list of integers

    example :
    input -> [1, 2, 3, 4, 5]
    output -> [2, 2, 6, 4, 10]
    """
    
    for index, integer in enumerate(integer_list):
        if integer % 2 == 1:
            integer_list[index] = integer * 2
    return integer_list
