def sum_of_fib_to(max_val):
    num=1
    prev_num=0
    fib_list = []
    while True:
        new_num=num+prev_num
        prev_num = num
        num=new_num
        if num >= max_val:
            return sum(fib_list)
        if new_num%2 == 0:
            fib_list.append(new_num)

print(sum_of_fib_to(4000000))
