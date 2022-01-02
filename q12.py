from q3 import *

def traverse_triangle_numbers(current_numbers):
    triangle_number = sum(current_numbers)
    while True:
        triangle_number = sum(current_numbers)
        if len(get_factors(triangle_number)) >= 500:
            return triangle_number
        current_numbers = current_numbers + [current_numbers[-1] + 1]

if __name__ == '__main__':
    number = traverse_triangle_numbers([1])
