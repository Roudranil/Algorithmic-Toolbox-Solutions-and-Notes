# Uses python3
import sys

def get_change(m):
    #write your code here
    total = 0
    total += m//10
    m = m%10
    total += m//5
    m = m%5
    total += m
    return total


m = int(input())
print(get_change(m))
