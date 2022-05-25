# Uses python3
import sys

def optimal_summands(n):
    summands = []
    a = 1
    while n>0:
        if a >= n/2:
            summands.append(n)
            break
        else:
            summands.append(a)
            n -= a
            a += 1
    return summands

def main():
    n = int(sys.stdin.readline())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

if __name__ == '__main__':
    main()