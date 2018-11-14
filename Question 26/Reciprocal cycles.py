def get_reciprocal_fraction(numerator,denominator):
    integral_part = numerator//denominator
    sigma = ''
    tau = ''
    if numerator == denominator:
        integral_part = numerator // denominator
        return integral_part
    else:
        n = numerator
        d = denominator
        decimal_list = [str(integral_part) + 'split+']
        rolling = [n%d]
        n %= d
        while n != 0:
            n *= 10
            decimal_list.append(str(n//d))
            n %= d
            if n not in rolling:
                rolling.append(n)
            else:
                decimal_list.insert(rolling.index(n)+1,'split-')
                break
        integral_part,dec = ''.join(str(d) for d in decimal_list).split('split+')
        if 'split-' in dec:
            sigma,tau = dec.split('split-')
        else:
            sigma = dec
##        return integral_part,sigma,tau
        if not tau:
            return 0
        else:
            return tau

r = get_reciprocal_fraction(1,7)
##if len(str(r)) == 1:
##    print(f'{r}')
##elif not r[1] and not r[2]:
##    print(f'{r[0]}')
##else:
##    print(f'{r[0]}.{r[1]}({r[2]})')

answer = max([(get_reciprocal_fraction(1,e),e) for e in range(1,1000)],key=lambda x:len(str(x)))

##for i in range(2,1000):
##    print('This is the denom:',i)
##    print(get_reciprocal_fraction(1,i)[2])
##    
