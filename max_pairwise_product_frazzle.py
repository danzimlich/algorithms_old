# Uses python3
import numpy as np

# n = int(input("n: "))
# a = [int(x) for x in input("a: ").split()]
# print("len(a): " + str(len(a)))
# assert(len(a) == n)

resultFast = 0
resultBrute = 0

while(resultFast == resultBrute):
    n = np.random.randint(low=2, high=10000)

    a = []
    for x in range (0, n):
        a.append(np.random.randint(low=0, high=10000))


    print("n: ", n)
    print(a)

    resultFast = 0
    resultBrute = 0

    #pairwise fast

    max1 = 0
    max2 = 0
    max1Count = 1

    for i in range (0, n):
        if a[i] == max1:
            max1Count = max1Count + 1
        if a[i] > max1:
            max2 = max1
            max1 = a[i]
            max1Count = 1
        if (a[i] > max2 and a[i] < max1):
            max2 = a[i]

    if max1 > max2:
        resultFast = max1 * max2
    if max1Count > 1:
        resultFast = max1 ** 2


    #pairwise brute force


    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > resultBrute:
                resultBrute = a[i]*a[j]

    if resultFast == resultBrute:
        print("OK")

    print(resultFast, " ", resultBrute)
