def get_spiral_by(index):
    i = 1
    spiral = 1
    spiral_of = 1

    while True:
        if spiral_of == index:
            return sp
        spiral_of += 2
        sp = [e for e in range(i+1,i+(spiral*9)-(spiral-1))]
        i = sp[-1]
        spiral += 1

if __name__ == '__main__':

    total = [1]
    for i in range(3,1003,2):
        s = get_spiral_by(i)
        end = s.pop()
        s.insert(0,end)
        total.append(sum(s[::i-1]))
    print(sum(total))
