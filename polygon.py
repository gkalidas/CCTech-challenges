# Needed this
from itertools import cycle


def orientation(p, q, r):
    """
    This function check the orientation of ordered triplets and
    returns
    0   if points are collinear
    1   if clockwise
    2  if counterclockwise
    """
    
    value = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if value == 0:
        return 0
    if value > 0:
        return 1
    else:
        return 2

def on_segment(p, q, r):
    """
    Function is used to check if point q lies on a segment(p,q) or not
    Returns
    True if point lies on a segment else False
    """
    if q[0] <= max(p[0], r[0]) and\
        q[0] >= min(p[0], r[0]) and\
            q[1] <= max(p[1], r[1]) and\
                q[1] >= min(p[1], r[1]):
                return True
    else:
        return False


def do_intersect(p1, q1, p2, q2):
    """
    Function to check if given segments (p1,q1) and (p2,q2)
    intersect with each other or not
    Returns
    True if segments intersect else False
    """

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    
    # general case
    if o1 != o2 and o3 != o4:

        return True

    # special cases
    # check if 
    if (o1 == 0 and on_segment(p1, p2, q1)):
        return True

    elif (o2 == 0 and on_segment(p1, q2, q1)):
        return True

    elif (o3 == 0 and on_segment(p2, p1, q2)):
        return True

    elif (o4 == 0 and on_segment(p2, q1, q2)):
        return True

    else:
        return False

def is_inside_polygon(polygon, n , p):
    """
    Function to check if point p lies inside a polygon or not
    Return
    True if point lies inside the polygon else False
    """
    
    # check if there are atleast three vertices for the polygon
    if n < 3:
        return False

    # an infinite point
    extreme = (10000, p[1])

    count = 0
    
    licycle = cycle(polygon)
    nextelem = next(licycle)

    for point in polygon:
        p1, p2 = nextelem, next(licycle)
        if (do_intersect(p1, p2, p, extreme)):
            if(orientation(p1, p, p2) == 0):
                result = on_segment(p1, p, p2) 
                return result
            count += 1
    if count % 2 == 1:
        return True
    return False

# example one
polygon1 = [[0, 0],[10, 0], [10, 10], [0, 10]]
n = len(polygon1)
point = [20,20]   # False
# point = [5, 5]    # True

# example two
# polygon2 = [[0, 0], [5, 5], [5, 0]]
# n = len(polygon1)
# point = [20,20]   # False

# example three
# polygon3 = [[1,0], [8,3], [8,8], [1,5]]
# n = len(polygon1)
# point = [3,5]     # True

# example four
# polygon4 = [[-3,2], [-2,-0.8], [0,1.2], [2.2,0], [2,4.5]]
# n = len(polygon1)
# point = [0, 0]     # False

if is_inside_polygon(polygon1, n, point):
    print(f"The point {point} is inside the polygon")
    print(True)
else:
    print(f"The point {point} is outside the polygon")
    print(False)
