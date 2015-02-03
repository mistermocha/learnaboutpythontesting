def fib(num):
    if num == 0:
        return num
    if num == 1:
        return num
    return fib(num-1) + fib(num-2)

def fiblist(num):
    ret = []
    for i in range(num):
        ret.append(fib(i))
    return ret
