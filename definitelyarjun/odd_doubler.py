def odd_doubler(input_list):
    
    solution_list = []
    for num in input_list:
        if num % 2 != 0:
            solution_list.append(num * 2)
        else:
            solution_list.append(num)

    return solution_list

