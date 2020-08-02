class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(p, q, r):
    """
    This function check the orientation of ordered triplets and
    returns
    0   if points are collinear
    1   if clockwise
    -1  if counterclockwise
    """
    value = ((q.y - p.y) * (r.x - q.x)) - \
    ((q.x - p.x) * (r.y - q.y))

    if value == 0:
        return 0
    if value > 0:
        return 1
    else:
        return -1

def on_segment(p, q, r):
    """
    Function is used to check if point q lies on a segment(p,q) or not
    Returns
    True if point lies on a segment else False
    """
    if q.x <= max(p.x, r.x) and\
        q.x >= min(p.x, r.x) and\
            q.y <= max(p.y, r.y) and\
                q.y >= min(p.y, r.y):
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

    if (o2 == 0 and on_segment(p1, q2, q1)):
        return True

    if (o3 == 0 and on_segment(p2, p1, q2)):
        return True

    if (o4 == 0 and on_segment((p2, q2, q2))):
        return True
    
    return False

def is_inside_polygon(polygon, n , p):
    """
    Function to check if point p lies inside a polygon or not
    Return
    True if point lies inside the polygon else False
    """
    
    # print("POLYGON",polygon,"N", n,"P", p)
    # check if there are atleast three vertices for the polygon
    if n < 3:
        return False

    # an infinite point
    extreme = (10000, p[1])
    # print("EXTREME ", extreme)

    count, i = 0, 0
    
    while polygon:
        print (" i is ", i)
        print("Polygon points ", polygon)
        p1 = polygon[i]
        if i + 1 == len(polygon):
            p2 = polygon[0]
        else:
            p2 = polygon[i + 1]
        if (do_intersect(p1, p2, p, extreme)):
            if(orientation(polygon[i], p, polygon[next_vertices]) == 0):
                return on_segment(polygon[i], p, polygon[next_vertices])
            count += 1
        i += 1

    if count % 2 == 0:
        return True
    return False

polygon1 = [[0, 0],[10, 0], [10, 10], [0, 10]]
n = len(polygon1)
print("length of the polygon", n)
point = [20,20]

if is_inside_polygon(polygon1, n, point):
    print("Inside the polygon")
else:
    print("Outside the polygon")