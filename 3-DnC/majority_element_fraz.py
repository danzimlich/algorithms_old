# Uses python3
import sys

def get_majority_element(a, left, right):
#    if left == right:
#        return -1
#    if left + 1 == right:
#        return a[left]

    #write your code here
    if len(a) == 0:
        return 0

    a.sort()
#    print(a)
    highest_i_count = 1
    i_count = 1
    current_i = a[0]

    for i in range(1, len(a)):
#        print("a[i] now", i, a[i] )
        if current_i == a[i]:
            i_count = i_count+1
#            print("i_count increased to", i_count)
        else:
            current_i = a[i]
            if i_count > highest_i_count:
                highest_i_count = i_count
#                print("highest i count now", highest_i_count)
            i_count = 1
        if i_count > (len(a) // 2):
            return 1


    if i_count > (len(a) // 2):
        return 1

    return -1




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
