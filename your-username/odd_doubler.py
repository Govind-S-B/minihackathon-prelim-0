def odd_doubler(odds):
    """
    doubles the value of all the odd numbers in the list and returns it
    """
    return [2*i if i%2!=0 else i for i in odds]