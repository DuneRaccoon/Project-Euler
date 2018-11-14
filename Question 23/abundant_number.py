from get_factors import *
import itertools

all_abundant_numbers = []

for number in range(1,28124):
    if sum(get_factors(number)[:-1]) > number:
        all_abundant_numbers.append(number)

total_sums = [False]*28124
can_be = [all_abundant_numbers[x]+all_abundant_numbers[y]\
          for x in range(0,len(all_abundant_numbers))\
          for y in range(x,len(all_abundant_numbers))
          if all_abundant_numbers[x]+all_abundant_numbers[y] <= 28123]

for n in set(can_be):
    total_sums[n] = True
    
print(sum([i for i,e in enumerate(total_sums) if not e]))
