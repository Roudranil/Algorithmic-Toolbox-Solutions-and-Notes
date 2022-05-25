# Uses python3
import sys

def get_optimal_value(n, capacity, weights, values):
    value = 0.
    # write your code here
    unitvalue = []
    for i in range(n):
        unitvalue.append(values[i]/weights[i])

    for i in range(n):
        if capacity == 0:
            return value
        maxunitvalue = unitvalue[0]
        maxindex = 0
        for i in range(n):
            if unitvalue[i] > maxunitvalue and weights[i]>0:
                maxunitvalue = unitvalue[i]
                maxindex = i
        a = min(weights[maxindex], capacity)
        value += a*unitvalue[maxindex]
        weights[maxindex] -= a
        capacity -= a

    return value

def main():
    values = []
    weights = []
    n, capacity = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        v, w = list(map(int, sys.stdin.readline().split()))
        values.append(v)
        weights.append(w)
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))

if __name__ == "__main__":
    main()