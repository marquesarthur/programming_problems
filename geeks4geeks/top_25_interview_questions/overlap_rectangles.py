# One solution is to one by one pick all points of one rectangle and see if the point lies inside the other rectangle or not.
# This can be done using the algorithm discussed here.
#   https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
#
# Following is a simpler approach. Two rectangles do not overlap if one of the following conditions is true.
# 1) One rectangle is above top edge of other rectangle.
# 2) One rectangle is on left side of left edge of other rectangle.
def in_range(val, start, end):
    if start > end:
        start, end = end, start
    return start <= val <= end

def overlap(l1, r1, l2, r2):

    l1, r1 = sorted([l1, r1], key=lambda p: (p[0], p[1]))
    l2, r2 = sorted([l2, r2], key=lambda p: (p[0], p[1]))

    x_overlaps = in_range(l2[0], l1[0], r1[0]) or in_range(r2[0], l1[0], r1[0])
    x_overlaps = x_overlaps or in_range(r1[0], l2[0], r2[0]) or in_range(r2[0], l2[0], r2[0])

    y_overlaps = in_range(l2[1], l1[1], r1[1]) or in_range(r2[1], l1[1], r1[1])
    y_overlaps = y_overlaps or in_range(r1[1], l2[1], r2[1]) or in_range(r2[1], l2[1], r2[1])




    return x_overlaps and y_overlaps


x = overlap((99, 39), (10, 34), (19, 41), (26, 18))
# y = overlap((19, 41), (26, 18), (99, 39), (10, 34))
print(x)






