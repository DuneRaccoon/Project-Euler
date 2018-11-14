print(sum([i for i in range(2,354294) if sum([e**5 for e in [int(e) for e in str(i)]]) == i]))
