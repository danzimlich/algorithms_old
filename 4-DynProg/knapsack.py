# Uses python3
import sys
import numpy as np


def dp_optimal_weight(W, wt_list):
    #w is the array of weights
    #W is the capacity of the knapsack in weight
    #n is the len(w)
    wt_list.insert(0,0)
#    print(wt_list)
    #initialize an n by W matrix
#    value_array = [[0 for j in range(W+1)] for i in range(len(w)+1)]
    value_array = np.zeros((len(wt_list), W+1), dtype = int)
#    value_array = np.arange(0, 32, 1).reshape(4,8)
#    print_matrix(value_array)
#    print(value_array)
#    print("value_array at index 2, 4 is", value_array[2,4])

    for i in range(1,len(wt_list)):
        for w in range(1,W+1):
#            value_array[w, i] = value_array[w, i-1]
            value_array[i, w] = value_array[i-1, w]
            if wt_list[i] <= w:
#                print(wt_list[i], w)
#                val = value_array[w - wt_list[i], i - 1] + wt_list[i]
                val =  value_array[i - 1, w - wt_list[i]] + wt_list[i]
                if value_array[i, w] < val:
                    value_array[i, w] = val

#    print(value_array)
    return value_array[n, W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(dp_optimal_weight(W, w))
