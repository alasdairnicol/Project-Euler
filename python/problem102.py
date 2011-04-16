"""
Three distinct points are plotted at random on a Cartesian plane, for
which -1000 <= x, y <= 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas
triangle XYZ does not.

Using triangles.txt, a 27K text file containing the co-ordinates of
one thousand "random" triangles, find the number of triangles for
which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in
the example given above.
"""

def cross_product((x1, y1), (x2, y2)):
    return x1 * y2 - x2 * y1

class Triangle(object):
    """
    Represents a triangle
    """
    def __init__(self, x1, y1, x2, y2, x3, y3 ):
        """
        Construct the points A, B, C
        """
        self.A = int(x1), int(y1)
        self.B = int(x2), int(y2)
        self.C = int(x3), int(y3)

    @property
    def points(self):
        """
        Returns a list of the points of the triangle
        """
        return [self.A, self.B, self.C]

    @property
    def edges(self):
        """
        Returns a list of (x,y) tuples representing the edges of the
        triangle as vectors.
        """
        return [
            (self.B[0]-self.A[0], self.B[1]-self.A[1]),
            (self.C[0]-self.B[0], self.C[1]-self.B[1]),
            (self.A[0]-self.C[0], self.A[1]-self.C[1]),
            ]

    def contains_point(self, p_x, p_y):
        """
        Returns True if the Triangle contains the point (p_x, p_y)

        To determine whether the Triange contains the points, we
        calculate the cross products of the edge and the vector from
        the starting vertex to the given point for each edge in the
        triangle.

        If the three cross products are in the same direction
        (i.e. the absolute value is > 0 for all or them or < 0 for all
        of them) then the triangle contains the point. Otherwise, the
        triangle does not contain the point.
        """
        cross_products = []
        for starting_vertex, edge in zip(self.points, self.edges):
            # Calculate the vector from the starting edge to the point
            # (p_x, p_y)
            v = (p_x - starting_vertex[0], p_y - starting_vertex[1])
            cp = cross_product(edge, v)
            cross_products.append(cp)
        # If the cross products all point in the same direction, then
        # the triangle contains the point
        directions = [cmp(c, 0) for c in cross_products]
        if directions == [1, 1, 1] or directions == [-1, -1, -1]:
            return True
        return False

    def contains_origin(self):
        """
        Returns True if the Triangle contains the origin.
        """
        return self.contains_point(0,0)

def solution():
    """
    Read the triangles from the text file, and count the number of
    them that contain the origin.
    """
    count = 0
    f = open('triangles.txt', 'r')
    for line in f.readlines():
        triangle = Triangle(*line.split(","))
        if triangle.contains_origin():
            count += 1
    f.close()
    return count

if __name__ == "__main__":
    print solution()
