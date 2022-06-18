# Uses python3
import sys

def optimal_sequence(n):
    sequences = [[]] * (n+1)
    sequences[1] = [1]
    for x in range(2,n+1):
        current_len = -1
        current_seq = []
        if x % 3 == 0:
            current_seq = sequences[x//3].copy()
            current_seq.append(x)
            current_len = len(current_seq)
        if x % 2 == 0:
            if len(sequences[x//2])+1 < current_len or current_len == -1:
                current_seq = sequences[x//2].copy()
                current_seq.append(x)
                current_len = len(current_seq)
        if len(sequences[x-1])+1 < current_len or current_len == -1:
            current_seq = sequences[x-1].copy()
            current_seq.append(x)
            current_len = len(current_seq)
        sequences[x] = current_seq
    
    return sequences[-1]

input = sys.stdin.readline()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
