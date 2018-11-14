##import itertools
##all_perms = [[e for e in itertools.product([1,2,5,10,20,50,100,200], repeat=1*i)\
##              if sum(e) == 200]\
##             for i in [1,2,5,10,20,50,100,200]] 
##final = []
##for p in all_perms:
##    for e in p:
##        final.append(tuple(sorted(e)))
##print(len(set(final)))
import string

mmp = []
for n in range(7254,1000000000):
    for a in [e for e in [0 if any(i in str(n) for i in str(e)) \
                          else e for e in range(1,n)] if e]:
        for b in [e for e in [0 if any(i in str(a) for i in str(e)) or\
                          any(i in str(n) for i in str(e)) \
                              else e for e in range(1,n)] if e]:
            print((a,b,n))
            if a*b == n and \
               sorted(list(str(a)+str(b)+str(n))) == list(string.digits[1:]):
                mmp.append((a,b,n))
                print((a,b,n))
