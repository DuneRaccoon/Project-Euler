from math import floor

def is_prime(number):
    print(number)
    return len([e for e in range(1,number+1) if number%e == 0]) == 2

def get_factors(number):
    factors = []
    new_num = number
    if number == 1:
        return [1]
    while True:
        seen_factors = []
        for e in range(2,new_num):
            if number%e == 0:
                if e in factors:
                    seen_factors.append(e)
                    seen_factors.append(number//e)
                else:
                    factors.append(e)
                    factors.append(number//e)
                    new_num = number//e
                    if new_num == e:
                        return sorted(list(set([1] + factors + [number])))
                    break
        if len(set(factors) - set(seen_factors)) == 0:
            return sorted(list(set([1] + factors + [number])))

##def get_factors(number):
##    return [i for i in range(1,floor(number/2)+1) if n%i == 0]

if __name__ == '__main__':

    factors = get_factors(600851475143)
    prime_factors = [e for e in factors if len(get_factors(e)) == 2]
    print(max(prime_factors))
    
