
def get_pythagorean_triplets(number):
    for a in range(1,number):
        for b in range(1,number-a):
            c = number - a - b
            if a*a + b*b == c*c:
                print(a,b,c)
                return a*b*c
    return False
