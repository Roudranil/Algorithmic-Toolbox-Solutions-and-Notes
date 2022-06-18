# Uses python3
import sys

def fast_count_segments(master, p, points):
    count = 0
    segment_count = ""
    point_map = {}
    master.sort()
    for element in master:
        if element[1] == 'l':
            count += 1
        elif element[1] == 'r':
            count -= 1
        else:
            point_map[element[0]] = count
    
    for point in points:
        segment_count += str(point_map[point]) + ' '
    return segment_count


if __name__ == '__main__':
    s, p = list(map(int, input().split()))
    master = []
    for i in range(s):
        x, y = list(map(int, input().split()))
        master.append([x, "l"])
        master.append([y, "r"])
    points = list(map(int, input().split()))
    master.extend([[point, "p"] for point in points])
    #use fast_count_segments
    count = fast_count_segments(master, p, points)
    print(count)
