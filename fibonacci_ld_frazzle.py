# Uses python3
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    a = [0,1]
    fib = 0

    if (n <= 1):
        return n
    if (n == 2):
        return 1

    for i in range(1, n):
        i = i+1
#        if i > 10:
#            i = i % 10
        fib_ld = (a[i-1]) + (a[i-2])
#        print("i is", i, a[i-1], a[i-2], "fib_ld is ", fib_ld)
#        fib_ld = fib_ld % 10

#        c = a[i]
#        if (a[i] < a[i-1]):
#            c = a[i] + 10
#        fib_ld = c - (a[i-1])
        fib_ld = fib_ld % 10
        a.append(fib_ld)
#    return fib
#    print(a)
    return fib_ld

n = int(input())
print(calc_fib_fast(n))
