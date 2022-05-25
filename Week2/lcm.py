# Uses python3
import sys

def gcd_naive(a, b):
    if a == b:
        return a
    elif a>b:
        return gcd_naive(a-b, b)
    else:
        return gcd_naive(a, b-a)

if __name__ == "__main__":
    a,b = map(int, input().split())
    gcd = gcd_naive(a,b)
    lcm = int((a*b)/gcd)
    print(lcm)
