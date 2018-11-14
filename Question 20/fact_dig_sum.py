def fact(n):
    if n == 1: return n
    else: return n * fact(n-1)

print(sum([int(e) for e in list(str(fact(100)))]))
