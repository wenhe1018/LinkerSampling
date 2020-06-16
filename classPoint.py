import math
class Point:
    x=99999.0
    y=99999.0
    z=99999.0
    def __init__ (self, x, y ,z):
        # Initializes the Point class
        self.x = x
        self.y = y
        self.z = z  
    def distance_to_another_point(self, other_point):
        # dist (float) to another point
        deltax = self.x - other_point.x
        deltay = self.y - other_point.y
        deltaz = self.z - other_point.z
        return math.sqrt(math.pow(deltax,2) + math.pow(deltay,2) + math.pow(deltaz,2))
