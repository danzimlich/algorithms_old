# Uses python3
import sys

def dp_optimal_sequence(n):
    dp_array = [0] * (n+1)


    for i in range(1, n + 1):
        #advancing to a higher number requires either the same amount of ops (upgrading from *2 to *3) or a new one.
        dp_array[i] = dp_array[i - 1] +1

 #       print("i is currently", i)
        if (i % 3 == 0):
            dp_array[i] = min(dp_array[i // 3] +1 , dp_array[i])

        elif (i % 2 == 0):
            dp_array[i] = min(dp_array[i // 2] +1 , dp_array[i])


    sequence = []
#    print(dp_array)
#    print("entering why loop")
    while n > 1:
        sequence.append(n)
#        print(n, "appended to sequence")

        if (dp_array[n - 1] == dp_array[n] - 1):
            n = n - 1
        elif (n % 2 == 0 and (dp_array[n // 2] == dp_array[n] - 1)):
            n = n // 2

        elif (n % 3 == 0 and (dp_array[n // 3] == dp_array[n] - 1)):
            n = n // 3

    sequence.append(1)

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)

sequence = list(dp_optimal_sequence(n))

print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
