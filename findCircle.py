import math as m
def findCircleFromTriple(p1, p2, p3):
    """
    Returns the center and radius of the circle passing the given 3 points.
    In case the 3 points form a line, returns (None, infinity).
    """
    temp = p2[0] * p2[0] + p2[1] * p2[1]
    bc = (p1[0] * p1[0] + p1[1] * p1[1] - temp) / 2
    cd = (temp - p3[0] * p3[0] - p3[1] * p3[1]) / 2
    det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])

    if abs(det) < 1.0e-6:
        return (None, 10000)

    # Center of circle
    cx = (bc*(p2[1] - p3[1]) - cd*(p1[1] - p2[1])) / det
    cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det

    radius = m.sqrt((cx - p1[0])**2 + (cy - p1[1])**2)
    return ((cx, cy), radius)

def isInCircle(circle, point):
    #print(circle)
    #print("XD")
    #print(point)
    if ((point[0][0]-circle[0][0])*(point[0][0]-circle[0][0]))+((point[0][1]-circle[0][1])*(point[0][1]-circle[0][1]))<=circle[1]*circle[1]:
        return True
    else:
        return False

def isEnclosingCircle(circle,points):
    ret=True
    for point in points:
        if not isInCircle(circle,point):
            ret=False
    return ret

def findCircle(points):
    n=len(points)
    circle=((0,0),0)
    for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and j!=k and k!=i:
                        c=findCircleFromTriple(points[i][0],points[j][0],points[k][0])
                        flag=True
                        for point in points:
                            if not isInCircle(c,point):
                                flag=False
                        if flag:
                            circle=c
    return circle