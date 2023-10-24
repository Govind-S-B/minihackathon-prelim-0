def odd_doubler(input_list):
    """
    task : complete the function odd_doubler which doubles the value of all the odd numbers in the list it receives and returns it
    - accepts a list of integers
    - returns a list of integers

    example :
    input -> [1, 2, 3, 4, 5]
    output -> [2, 2, 6, 4, 10]
    """
    
    output_list=[]
    for num in input_list:
        if num % 2==0:
            output_list.append(num)
        else:output_list.append(num*2)

    return output_list
    


