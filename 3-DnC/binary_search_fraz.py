# Uses python3
import sys

def binary_search(a, x):
    # write your code here
    b = a

# if the number we're looking for is outside of the sorted array, immediately return -1
    if x > a[len(a) - 1] or x < a[0]:
        return -1
    if x == a[len(a)-1]:
        return len(a)-1
    # track the lower and upper bound of each subarray to track the index in original array
#    left_lower = 0
#    left_upper = (len(a) // 2) - 1
#    right_lower = len (a) // 2
#    right_upper = len(a) - 1

    lower_i = 0
    upper_i = len(a) - 1
    middle_i = (len(a) - 1) // 2
    iteration_count = 0
    while len(b) > 0:
        middle_index = (len(b) - 1) // 2
        left_array = b[0:middle_index]
#        print("left_array", left_array)
        right_array = b[middle_index:(len(b))]
#        print("right_array", right_array)
#        print("middle_index", middle_index, "value", b[middle_index])

#        if x > a[len(b)-1] or x < b[0]:
#            return -1

        if lower_i == upper_i:
#            print("case lower_i = upper_i")
            return lower_i


        if len(left_array) and len(right_array) <= 1:
            if len(left_array) == 1:
                if left_array[0] != x:
                    return -1
            elif len(right_array) == 1:
                if right_array[0] != x:
                    return -1

        if (len(left_array) > 0) and (len(right_array) > 0):
            if x > left_array[len(left_array)-1] and x < right_array[0]:
                return -1

        if x < b[middle_index]:

            b = left_array
            upper_i = middle_index-1
 #           print("upper_i shifted to", upper_i)
        elif x > b[middle_index]:

            b = right_array
            lower_i = middle_index + lower_i
#            print("lower_i shifted to", lower_i)
            if len(b) == 2:
                if b[1] == x:
                    return lower_i+1

        elif x == b[middle_index]:
            #            lower_i = middle_index
            #            lower_i = middle_index + (len(left_array)-1)
            lower_i = middle_index + lower_i
#            print(x, "x equal to b at middle index", lower_i)
            return lower_i



        iteration_count = iteration_count + 1
#        print("iteration_count is", iteration_count)
        if iteration_count > 5:
            print("hitting iteration count limit")
            break
    #if len(b) <= 2:
    #    for j in b:
    #        if x == b[j]:
    #            return



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]

    m = data[n + 1]
    a = data[1 : n + 1]
#    print (data[n+2:])
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
#        print("-----------")
#        print("now looking for", x)
        print(binary_search(a, x), end = ' ')
