__author__ = 'zieghailo'

import numpy as np
from point import Point


class BetaSkeleton():

    def __init__(self, points=[], beta=1):
        self.points = points
        self.beta = beta

    @property
    def point_val(self):
        val = [point.p for point in self.points]
        return np.array(val)

    def randomize(self, n, maxx, maxy):
        for i in range(n):
            p = Point(np.random.rand(2) * [maxx, maxy])
            self.points.append(p)


def create_brute_skeleton(points, beta=1):
    for a in points:
        for b in points:
            can_connect = True
            for c in points:
                angle = get_angle(a.p, b.p, c.p)
                if angle < beta:
                    can_connect = False
                    break

            if can_connect:
                a.connections.append(b)
                b.connections.append(a)


def get_angle(p1, p2, p3):
     """
     Gets the angle between three points, where p3 is the middle one whose angle were looking for
     :param p1: point 1
     :param p2: point 2
     :param p3: middle point whose angle we're looking for
     :return: angle
     """

     p12 = np.sqrt(np.sum((p1 - p2) ** 2))
     p13 = np.sqrt(np.sum((p1 - p3) ** 2))
     p23 = np.sqrt(np.sum((p2 - p3) ** 2))

     angle = np.arccos((p23 ** 2 + p13 ** 2 - p12 ** 2) / (2 * p23 * p13))
     return angle