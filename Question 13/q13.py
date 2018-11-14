with open('number.txt') as numbers:
    numbers = str(sum([int(e) for e in numbers.read().split()]))[:10]
