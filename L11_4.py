__author__ = 'Hernan Y.Ke'
#redefine your own exception
import math
class TriangleExp(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._side = tuple(sides)

    @property
    def sides(self):
        return self.sides

    def __str__(self):
        return "'{}' for sides {}".format(self.args[0],self._sides)

    def __repr__(self):
        return "TriangularError({!r},{!r}".format(self.args[0],self._sides)

def triangular_area(a,b,c):
    sides = sorted((a,b,c))
    if sides[2]>sides[0]+sides[1]:
        raise TriangleExp("Error",sides)
    p= (a+b+c)/2
    a=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return a