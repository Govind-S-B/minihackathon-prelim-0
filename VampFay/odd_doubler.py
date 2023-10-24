def odd_doubler(input_list):
    """
    task : complete the function odd_doubler which doubles the value of all the odd numbers in the list it receives and returns it
    - accepts a list of integers
    - returns a list of integers

    example :

    input -> [1, 2, 3, 4, 5]
    output -> [2, 2, 6, 4, 10]
    """
         
    newl=[]
    for i in input_list:
        if i % 2 !=0:
            newl.append(2*i)
            #i=i*2
        else:
            newl.append(i)
    return newl       
    

#odd_doubler()