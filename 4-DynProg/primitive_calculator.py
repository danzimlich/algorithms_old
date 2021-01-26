# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dp_optimal_sequence3(n):
    sequence = []
    while n > 5:
        sequence.append(n)
        rem = n % 3
        if rem == 1:
            n = n - 1
        elif rem == 2:
#            n = n // 2
            if n % 2 == 0:
                n = n // 2
            else:
                n = n - 1
        else:
            n = n // 3

    if n == 5:
        sequence.append(5)
        sequence.append(4)
        sequence.append(3)
        sequence.append(1)
    elif n == 4:
        sequence.append(4)
        sequence.append(2)
        sequence.append(1)
    elif n == 3:
        sequence.append(3)
        sequence.append(1)
    elif n == 2:
        sequence.append(2)
        sequence.append(1)
    elif n == 1:
        sequence.append(1)

    return reversed(sequence)


def dp_optimal_sequence2(n):
    sequence = []
    while n > 5:
        sequence.append(n)
        rem3 = n % 3
        rem2 = n % 2
        if rem3 == 0:
            n = n // 3
        elif rem2 == 0:
            n = n // 2
        elif rem3 == 1:
            n = n - 1
        elif rem3 == 2:
#            n = n // 2
            if rem2 == 0:
                n = n // 2
            else:
                n = n - 1
        else:
            n = n // 3

    if n == 5:
        sequence.append(5)
        sequence.append(4)
        sequence.append(3)
        sequence.append(1)
    elif n == 4:
        sequence.append(4)
        sequence.append(2)
        sequence.append(1)
    elif n == 3:
        sequence.append(3)
        sequence.append(1)
    elif n == 2:
        sequence.append(2)
        sequence.append(1)
    elif n == 1:
        sequence.append(1)

    return reversed(sequence)

def dp_optimal_sequence4(n):
    sequence = []
    while n > 5:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 3 > 0:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n - 1
        else:
            n = n - 1

    if n == 5:
        sequence.append(5)
        sequence.append(4)
        sequence.append(3)
        sequence.append(1)
    elif n == 4:
        sequence.append(4)
        sequence.append(2)
        sequence.append(1)
    elif n == 3:
        sequence.append(3)
        sequence.append(1)
    elif n == 2:
        sequence.append(2)
        sequence.append(1)
    elif n == 1:
        sequence.append(1)

    return reversed(sequence)

def dp_optimal_sequence5(n):
    sequence = []
    while n > 5:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 3 == 1:
                n = n - 1
                if n % 3 == 0:
                    sequence.append(n)
                    n = n // 3
        else:
            n = n - 1

    if n == 5:
        sequence.append(5)
        sequence.append(4)
        sequence.append(3)
        sequence.append(1)
    elif n == 4:
        sequence.append(4)
        sequence.append(2)
        sequence.append(1)
    elif n == 3:
        sequence.append(3)
        sequence.append(1)
    elif n == 2:
        sequence.append(2)
        sequence.append(1)
    elif n == 1:
        sequence.append(1)

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)

sequence3 = list(dp_optimal_sequence3(n))
sequence2 = list(dp_optimal_sequence2(n))
sequence4 = list(dp_optimal_sequence4(n))
sequence5 = list(dp_optimal_sequence5(n))

smallest = [len(sequence2), len(sequence3), len(sequence4), len(sequence5)]

smallest_ops = 1239129837237763482349
smallest_ops_index = 0
for i in range(0, len(smallest) - 1):
    if smallest[i] < smallest_ops:
        smallest_ops = smallest[i]
        smallest_ops_index = i
if smallest_ops_index == 0:
    sequence = sequence2
elif smallest_ops_index == 1:
    sequence = sequence3
elif smallest_ops_index == 2:
    sequence = sequence4
else:
    sequence = sequence5

print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
