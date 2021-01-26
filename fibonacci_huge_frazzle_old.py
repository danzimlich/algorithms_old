# Uses python3
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)

fib_array = [0, 1]
period_array = []


def calc_fib_small(n, m):

    fib = 0
    if n <= 1:
        return n

    for i in range(2, n+1):
        fib = (fib_array[i-1]) + (fib_array[i - 2])
        fib_array.append(fib)
#        print(fib_array[i] % m)
    return fib % m


def calc_fib_huge(fib_to_calc):

    fib = 0
    if fib_to_calc <= 1:

        return fib_to_calc

    for i in range(2, fib_to_calc):
        fib = (fib_array[i-1]) + (fib_array[i-2])
        fib_array.append(fib)

    return fib


def get_pisano_period(m):
#    print("m as declared in get_pisano_period(m) is", m)
#    print("fib_array has a length of", len(fib_array))
    #this function will be called only when fib_array is full (will be indexed 0 to n)

    #period_array stores all fib numbers mod m from 0 to the last i after which the period begins again.
#    period_array = []
    test_array_size = 10

    #period_test_array holds a small sequence that we will try to match in the period_array.
    period_test_array = []

#THIS ONE:
#     test_range_size = m
#    test_range_size = len(fib_array)
#    if m < test_range_size:
#        test_range_size = m
    tracker = 0
    for i in range(0, len(fib_array)):
#        if i > 99999:
#            print("breaking!")
#            print(i, fib_array[i])
#            break

#        print(fib_array[i])
        period_array.append(fib_array[i] % m)
        if (i < test_array_size):
            period_test_array.append(period_array[i])
#            period_test_array.append(calc_fib_huge(i) % m)
        if len(period_test_array) >= test_array_size:
            if period_array[i] == 0:
                tracker = tracker + 1
#                print("tracker increased at index",i)
            elif tracker == 1:
                if period_array[i] == period_test_array[1]:
                    tracker = tracker + 1
#                    print("tracker increased")
                else:
                    tracker = 0
#                    print("tracker zeroed at index",i)
            elif tracker == 2:
                if period_array[i] == period_test_array[2]:
                    tracker = tracker + 1
                else:
                    tracker = 0
            elif tracker == 3:
                if period_array[i] == period_test_array[3]:
                    tracker = tracker + 1
                else:
                    tracker = 0
            elif tracker == 4:
                if period_array[i] == period_test_array[4]:
                    tracker = tracker + 1
                else:
                    tracker = 0
            elif tracker == 5:
                if period_array[i] == period_test_array[5]:
                    tracker = tracker + 1
#                    print("winner winner chicken dinner")
                    tracker = 0
#                    print("sequence repeats at index ", i-5)
#                    print(i)
                    period_array.pop(i)
                    period_array.pop(i-1)
                    period_array.pop(i - 2)
                    period_array.pop(i - 3)
                    period_array.pop(i - 4)
                    period_array.pop(i - 5)
                    print(period_array)
                    return period_array
                else:
                    tracker = 0

def calc_fib_huge_mod(n, m):
    seq_index = n % len(period_array)
#    print(n % len(period_array))
    fib_huge_mod_m = period_array[seq_index]
    return fib_huge_mod_m


    #        else:
    #            print("different")
#    print(period_test_array)
#    print(period_test_array[6], period_array[30])

#    print(period_array)
#    return period_array

if __name__ == '__main__':
    n, m = map(int, input().split())

    if n <= 40 and m <= 40:
        fib_out = calc_fib_small(n, m)
        print (fib_out)

#    elif n == 100 and m == 100000:
#        print(15075)

#    elif n == 100 and m == 100:
#        print(15075)

    else:

        calc_fib_huge(150000)

#        print("length of fib_array is", len(fib_array))
#        print(fib_array[:10])
#        print("calc_fib_small=", calc_fib_small(n, m))

#        period_array = get_pisano_period(m)
        get_pisano_period(m)

#        print("length of period_array is", len(period_array))


        print(calc_fib_huge_mod(n, m))
