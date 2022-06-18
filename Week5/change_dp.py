# Uses python3
import sys
import math

def get_change(m):
    value = [0] + [math.inf] * m
    coins = [1,3,4]

    for x in range(1,m+1):
        for coin in coins:
            if coin <= x:
                val = value[x-coin] + 1
                if val < value[x]:
                    value[x] = val

    return value[-1]

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
