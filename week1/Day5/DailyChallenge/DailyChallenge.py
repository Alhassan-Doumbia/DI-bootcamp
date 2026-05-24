```python
import math


class Circle:

    def __init__(self, radius=None, diameter=None):

        if radius is not None:
            self.radius = radius

        elif diameter is not None:
            self.radius = diameter / 2

        else:
            self.radius = 0


    @property
    def diameter(self):
        return self.radius * 2


    @property
    def area(self):
        return math.pi * (self.radius ** 2)


    def __str__(self):

        return f"Circle radius : {self.radius}\nCircle diameter : {self.diameter}\nCircle area : {round(self.area,2)}"


    def __add__(self, other_circle):

        new_radius = self.radius + other_circle.radius

        return Circle(radius=new_radius)


    def __gt__(self, other_circle):

        return self.radius > other_circle.radius


    def __eq__(self, other_circle):

        return self.radius == other_circle.radius


    def __lt__(self, other_circle):

        return self.radius < other_circle.radius



circle1 = Circle(radius=10)
circle2 = Circle(diameter=40)

print(circle1)
print("==============")
print(circle2)

print("==============")

circle3 = circle1 + circle2

print(circle3)

print("==============")

print(circle1 > circle2)
print(circle1 == circle2)

print("==============")

all_circles = [
    Circle(radius=7),
    Circle(radius=2),
    Circle(radius=15),
    Circle(radius=1)
]

sorted_circles = sorted(all_circles)

for circle in sorted_circles:
    print(circle)
    print("------")
```
