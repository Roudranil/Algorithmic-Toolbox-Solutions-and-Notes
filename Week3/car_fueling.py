# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    laststop = 0
    maxtank = tank
    numrefill = 0
    i = 0
    while i < len(stops):
        if maxtank < stops[i] - laststop:
            return -1
        elif tank >= stops[i] - laststop:
            tank -= (stops[i] - laststop)
            laststop = stops[i]
            i += 1
        else:
            tank = maxtank
            numrefill += 1
            laststop = stops[i-1]
        
    return numrefill

def main():
    d = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    stops = list(map(int, sys.stdin.readline().split()))
    num_refill = compute_min_refills(d, m, stops)
    print(num_refill)

if __name__ == '__main__':
    main()