#Uses python3

import sys

def largest_number(n, a):
    for i in range(n-1):
        for j in range(n-i-1):
            if int(a[j][0]) <= int(a[j+1][0]) and int(a[j+1]+a[j]) > int(a[j]+a[j+1]):
                a[j+1], a[j] = a[j], a[j+1]   

    res = ""
    for x in a:
        res += x
    return res

def main():
    n = int(sys.stdin.readline())
    data = list(sys.stdin.readline().split())
    print(largest_number(n, data))
    
if __name__ == '__main__':
    main()
