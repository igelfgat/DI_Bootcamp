# Daily Challenge - Circle

"""The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter.
The user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area
Print the attributes of the circle - use a dunder method
Be able to add two circles together, and return a new circle with the new radius - use a dunder method
Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
Be able to put them in a list and sort them"""
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.diameter = radius * 2

    def circ_area(self):
        area = math.pi * math.pow(self.radius,2)
        return area
    def __str__(self):
        return f'This circle\'s diametr is {self.diameter} and radius is {self.radius}'
    def __repr__(self):
        return f'{self.diameter}:int \n {self.radius}:int'
    def __add__(self, other):
        if isinstance(other, (int, float)):  
            return self.radius + other
        elif isinstance(other, Circle):  
            return Circle(self.radius + other.radius)
    def __gt__(self, other: "Circle") -> bool:  
        return self.radius > other.radius
    def __eq__(self, other: "Circle") -> bool:  
        return self.radius == other.radius
def main():
    c1 = Circle(10)
    c2 = Circle(5)
    c3 = Circle(25)
    c4 = Circle(3)
    print(repr(c1))
    print(c1.circ_area())
    print(c1 + c2)
    print(c1 > c2)
    print(c1 == c2)
    circles = [c1, c2, c3, c4]

    circles.sort()

    for circle in circles:
        print(circle)


if __name__ in "__main__":
    main()