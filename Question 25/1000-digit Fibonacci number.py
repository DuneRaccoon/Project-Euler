def get_fib_of_length(length):
    start = 1
    prev = 0
    index = 1
    fibs = []
    while True:
        p = start
        fibs.append(start)
        start = start+prev
        prev = p
        index += 1
        if len(str(start)) == length:
            return (index,start)

