def odd_doubler(numlist):
    """
    task : complete the function odd_doubler which doubles the value of all the odd numbers in the list it receives and returns it
    - accepts a list of integers
    - returns a list of integers

    example :
    input -> [1, 2, 3, 4, 5]
    output -> [2, 2, 6, 4, 10]
    """
    double = [2*i if i%2 !=0 else i for i in numlist]
    return double



# numlist= list(map(int,input().split()))
# print(odd_doubler(numlist))
