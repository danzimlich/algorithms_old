# Uses python3
import sys

def get_change(m):
    change_10s = 0
    change_5s = 0
    change_1s = 0
    change_10s = m // 10
    rem_after_10s = m % 10
#    print ("10s", change_10s, rem_after_10s)
    if rem_after_10s > 4:
        change_5s = rem_after_10s // 5
        change_1s = rem_after_10s % 5
    else:
        change_1s = rem_after_10s
    coins = change_10s + change_1s + change_5s
    return coins

if __name__ == '__main__':
#    m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
