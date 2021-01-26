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

    for i in range(1, n):
        fib = (a[i]) + (a[i-1])
        a.append(fib)
#    print(a)
    return fib


n = int(input())
print(calc_fib_fast(n))