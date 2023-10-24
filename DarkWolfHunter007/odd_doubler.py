def odd_doubler(input_list):
    result = []
    for num in input_list:
        if num % 2 != 0:
            result.append(num * 2)
        else:
            result.append(num)
    return result

pass 
