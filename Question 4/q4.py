from functools import reduce
import itertools

def is_palindrome(number):
    return str(number) == str(number)[::-1]

if __name__ == '__main__':

    all_combos = itertools.combinations([e for e in range(100,1000)],2)
    multi_palindromes = [e for e in \
                         [reduce(lambda x,y:x*y,e) for e in all_combos]\
                         if is_palindrome(e)]
    print(max(multi_palindromes))
    
