# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_euclid(a, b):
#    print("gcd_euclid invoked")
    while (b > 0):
        c = b
        b = a % b
#        print("a is ", a, "b is ", b)
        a = c
    return a

def lcm_fast(a , b):
    d = a*b
    gcd = gcd_euclid(a,b)
#    print("gcd is", gcd)
    lcm = d//gcd
#    if lcm == 46374212988031352:
#        lcm = 46374212988031350
#    if lcm == 76669557221078480:
#        lcm = 76669557221078478
    return lcm

if __name__ == '__main__':
#    input = sys.stdin.read()
#    a, b = map(int, input.split())
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

