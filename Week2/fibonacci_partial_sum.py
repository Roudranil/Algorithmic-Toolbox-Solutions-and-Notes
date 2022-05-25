# Uses python3

def calc_fib(n):
    F = [0,1]
    if n >= 2:
        for i in range(2, n+1):
            F.append(F[i-1]+F[i-2])
    return F[n]

def get_last_digit(n, m):
    sums = [0, 1, 2]
    for i in range(3,60):
        sum = (1 + 2*sums[i-2] + calc_fib(i-1)) % 10
        sums.append(sum)

    return (sums[n%60] - sums[(m-1)%60])%10

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(get_last_digit(n,m))
    
