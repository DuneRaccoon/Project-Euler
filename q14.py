import operator

def get_chains(max_number):
    chains = {}
    for n in range(2,max_number):
        chain = [n]
        number = n
        while number != 1:
            if number % 2 == 0:
                number = number//2
                chain.append(number)
            else:
                number = (3*number) + 1
                chain.append(number)
        chains[n] = chain
    return chains

if __name__ == '__main__':
    m = 1000000
    chains = get_chains(m)
    longest_chain = max([(n,len(chains[n])) for n in range(2,m)],key=lambda x:x[1])
