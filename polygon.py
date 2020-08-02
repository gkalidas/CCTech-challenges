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
