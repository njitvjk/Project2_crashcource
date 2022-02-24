def division(num_1, num_2):
    """Perform division operation on num_1 and num_2"""
    # if b == 0:
    try:
        output = float(num_1) / float(num_2)
        print('The result of division is ', str(output))
        return output
    except ZeroDivisionError as ex_div:
        print('The result of division is ', ex_div)
        return ex_div

print(division(2,0))



