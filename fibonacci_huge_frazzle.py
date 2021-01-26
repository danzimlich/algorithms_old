# Uses python3

fib_array = [0, 1]
test_array_size = 10

def calc_fib_small(n, m):
    fib = 0
    if n <= 1:
        return n

    for i in range(1, n):
        fib = (fib_array[i]) + (fib_array[i - 1])
        fib_array.append(fib)
    return fib % m


def calc_fib_huge(n):
    fib = 0
    if n <= 1:
        return n

    for i in range(1, n):
        fib = (fib_array[i]) + (fib_array[i-1])
        fib_array.append(fib)



def get_pisano_period(m):
    period_array = []
#    test_array_size = 10
#   What DOES THIS DO!!?!?!?
    period_test_array = []

    test_range_size = m*4
#    if m < test_range_size:
#        test_range_size = m
    tracker = 0

    for i in (0, test_range_size):
#        print(i)
        period_array.append(fib_array[i] % m)
        add_to_test_array = fib_array[i] % m
        if (i < test_array_size):
            period_test_array.append(add_to_test_array)
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
#                    tracker = tracker + 1
                    print("winner winner chicken dinner")
#                    tracker = 0
                    print("sequence repeats at index ", i-5)
                    period_array.pop(i)
                    period_array.pop(i-1)
                    period_array.pop(i - 2)
                    period_array.pop(i - 3)
                    period_array.pop(i - 4)
                    period_array.pop(i - 5)
                    return period_array
                else:
                    tracker = 0

def calc_fib_huge_mod(n, m):
    if period_array == []:
        print("period_array is empty!")
    else:
        seq_index = n % len(period_array)
        fib_huge_mod_m = period_array[seq_index]
        return int(fib_huge_mod_m)


    #        else:
    #            print("different")
#    print(period_test_array)
#    print(period_test_array[6], period_array[30])

#    print(period_array)
#    return period_array

if __name__ == '__main__':
    n, m = map(int, input().split())

    if n < 100 and m < 100:
        fib_out = calc_fib_small(n, m)
        print (fib_out)

    else:
        print("going big here")
        calc_fib_huge(100000)
        period_array = get_pisano_period(m)
        print(calc_fib_huge_mod(n, m))
