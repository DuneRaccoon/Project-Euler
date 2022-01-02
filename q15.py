import itertools

def split_positions(l,d):
    group = []
    while l:
        group.append(l[:d+1])
        l = l[d+1:]
    return group

def get_routes(grid):
    paths = []
    solutions = []
    counter=0
##    for i in range(0,grid):
##        paths.append('R')
##        paths.append('D')

    for i in itertools.product('RDRD',repeat= grid*2):
        if i not in solutions:
            print(i)
            solutions.append(i)
            counter+=1
    return counter
        

def fact(n):
    if n == 1: return n
    return n * fact(n-1)

dim=2
positions = split_positions([e for e in range(1,((dim+1)**2) + 1)],dim)
coordinates = [(i,j) for i in range(len(positions)) for j in range(len(positions))]

##routes = itertools.product('RD',repeat=dim**2)
##get_routes(positions,(0,0),((dim+1)**2,(dim+1)**2))


num = int(fact(2*20) / (fact(20))**2)

num2 = get_routes(2)
