from get_factors import *

def amicable_test(up_to):
    amicable_numbers = []
    for number in range(1,up_to+1):
        second_number = sum(get_factors(number)[:-1])
        if second_number == number:
            pass
        elif sum(get_factors(second_number)[:-1]) == number:
            amicable_numbers += [number,second_number]
    return amicable_numbers
    
if __name__ == '__main__':
    nums = sorted(list(set(amicable_test(100000))))
