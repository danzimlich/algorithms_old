# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_euclid(a, b):
#    print("gcd_euclid invoked")
    while (b > 0):
        c = b
        b = a % b
#        print("a is ", a, "b is ", b)
        a = c
    return a


if __name__ == "__main__":
#    input = sys.stdin.read()
#    a, b = map(int, input.split())
    a, b = map(int, input().split())
    print(gcd_euclid(a, b))
