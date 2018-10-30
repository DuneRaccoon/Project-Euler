from functools import reduce

def get_smallest_number(step):
    new_checks = [11, 13, 14, 16, 17, 18, 19, 20]
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in new_checks):
            return num
    return None

if __name__ == '__main__':

    print(get_smallest_number(2520))
