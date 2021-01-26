# Uses python3
import sys



def get_optimal_value(capacity, weights, values):
    sum_weights = 0
    sum_values = 0
    value = 0.
    data_matrix = []
    for i in range(len(values)):
        data_matrix.append([values[i], weights[i], values[i] / weights[i]])
        sum_weights = sum_weights + weights[i]
        sum_values = sum_values + values[i]

#    print(data_matrix)

#   If the capacity of the pack is larger than what's available:
    if sum_weights < capacity:
#        print("not enough stuff to steal!")
        return sum_values
    #sort the data_matrix by value/weight
    data_matrix_by_vw = sorted(data_matrix, key=lambda x:x[2])
#    print(data_matrix_by_vw)

    vw_quotient = 0
    while capacity > 0:
        vw_row = data_matrix_by_vw.pop()
        vw_quotient = vw_row[2]
        #if we can't fit the whole item, fit the most you can:
        if capacity < vw_row[1]:
            value = value + vw_quotient * capacity
            capacity = capacity - vw_row[1]
#            print("splitting an item to add", value)
        else:
            value = value + vw_row[0]
            capacity = capacity - vw_row[1]
#        print(value)


    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
