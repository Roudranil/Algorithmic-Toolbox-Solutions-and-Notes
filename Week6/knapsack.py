# Uses python3
import sys

def optimal_weight(W, n, w):
    value = []
    for i in range(W+1):
        value.append([])
        value[i].append(0)
    for j in range(1, n+1):
        value[0].append(0)

    for i in range(1,n+1):
        for x in range(1,W+1):
            value[x].append(value[x][i-1])
            if w[i-1] <= x:
                val = value[x-w[i-1]][i-1] + w[i-1]
                if val > value[x][i]:
                    value[x][i] = val
     
    return value[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.readline()
    W, n = list(map(int, input.split()))
    weights = sys.stdin.readline()
    w = list(map(int, weights.split()))
    print(optimal_weight(W, n, w))
