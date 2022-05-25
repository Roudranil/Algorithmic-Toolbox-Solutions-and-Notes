# Uses python3
import sys

def get_fib(n, m):
    period = 0
    F = [0,1]
    current = 1
    previous = 1 
    i = 2
    while (previous!=0 or current!=1):
        previous = current
        current = (F[i-1] + F[i-2]) % m
        F.append(current)
        i = i + 1
        period = period + 1
    
    index_of_n = n % period
    return F[index_of_n]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fib(n,m))
