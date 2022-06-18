# Uses python3
import math

def min_and_max(i, j, operations):
    # print(f"called min_and_max({i},{j})")
    min_val = math.inf
    max_val = -math.inf
    
    for k in range(i, j):
        a = operations[k](M[i][k], M[k+1][j])
        b = operations[k](M[i][k], m[k+1][j])
        c = operations[k](m[i][k], M[k+1][j])
        d = operations[k](m[i][k], m[k+1][j])
        # print(f"for k={k}, a = {a}, b = {b}, c = {c}, d = {d}")

        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)

    # print(f"min = {min_val}, max = {max_val}\n")
    return (min_val, max_val)

def parentheses(n, digits, operations):
    global m
    global M

    for i in range(n):
        M[i][i] = m[i][i] = digits[i]
    
    # print(M)
    # print(m)
    # print(n)
    # print(list(range(1,n)))
    for s in range(1,n):
        # print(f"s = {s}")
        for i in range(n-s):
            # print(f"s = {s}, i = {i}")
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, operations)
    
    return M[0][-1]

plus = lambda a, b: a+b
minus = lambda a, b: a-b
times = lambda a, b: a*b

symbols = list(input())
digits = []
operations = []
for i in range(len(symbols)):
    if i%2 == 0:
        digits.append(int(symbols[i]))
    else:
        if symbols[i] == "+":
            operations.append(plus)
        elif symbols[i] == "-":
            operations.append(minus)
        else:
            operations.append(times)

n = (len(symbols) + 1)//2

M = []
m = []
for i in range(n):
    M.append([0]*n)
    m.append([0]*n)

print(parentheses(n, digits, operations))
