# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    F = [0,1]
    if n>=2: 
        for i in range(2,n+1):
            last_digit = (F[i-1] + F[i-2]) % 10
            F.append(last_digit)

    return F[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
