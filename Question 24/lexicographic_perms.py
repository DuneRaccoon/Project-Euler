import itertools
for i,p in enumerate(itertools.permutations('0123456789')):
    if i == 1999999:
        print(''.join(p))
        break 
