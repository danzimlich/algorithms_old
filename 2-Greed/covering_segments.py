# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    overlap_set = []

    segments_max_b = sorted(segments, key=lambda x:x[1])
    segments_max_b.reverse()
    print(segments_max_b)

    for i in range(len(segments_max_b)-1):
        constraints = [segments_max_b[i].start, segments_max_b[i+1].end]
        loop_logic = True
        while loop_logic == True and i < len(segments_max_b)-1:

#           Check for a disjoint segment and add a point for that one segment:
            if segments_max_b[i].start > segments_max_b[i + 1].end:
                print("DISJOINT")
                loop_logic = False
                points.append(segments_max_b[i].end)
                print("added point", segments_max_b[i].end)

#           If a start time of a segment is after the start time of a segment that has a later end time ("V")
            if segments_max_b[i].start <= segments_max_b[i+1].start:
                constraints[0] = segments_max_b[i+1].start
#                i = i + 1
                if (i > len(segments_max_b)-1):
                    loop_logic = False
                    # lastone:

#           Bring the end time constraint in.
#            if segments_max_b[i].end >= segments_max_b[i + 1].end:
#                constraints[1] = segments_max_b[i + 1].end

#            if segments_max_b[i].start <= segments_max_b[i + 1].end:
#                constraints[1] = segments_max_b[i + 1].end

#                points.append(segments_max_b[i + 1].end)
#                print("added point i.start <= i+1.end", segments_max_b[i+1].end)
#                loop_logic = False

#            if segments_max_b[i].end >= segments_max_b[i+1].end:
#                constraints[1] = segments_max_b[i+1].end
#                i = i + 1
#                if (i > len(segments_max_b)-1):
#                    loop_logic = False

            if constraints[0] == constraints[1]:
                points.append(constraints[0])
                print("added point", constraints[0], "constraints equal")
                loop_logic = False


#    for s in segments:
#        points.append(s.start)
#        points.append(s.end)
    #remove redundant points
    points.sort()
#    print(points)

    length_points = len(points)
#    print(length_points)

    for p in range(1, length_points):
        print(points[p])
        if points[p] == points[p-1]:
#            points.remove(points[p])
            points[p] = -1

#   Remove the "-1" dummy points (duplicates)
    points.sort()
    points.reverse()
#    print(points)
    dummy_points_check_index = len(points) - 1
    dummy_points_check_value = 0
    dummy_points_check_boolean = False

    while dummy_points_check_boolean == False:
        if points[dummy_points_check_index] < 0:
            points.pop()
            dummy_points_check_index = dummy_points_check_index-1
        else:
            dummy_points_check_boolean = True



    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print("len(points)", len(points))
    for p in points:
        print(p, end=' ')
