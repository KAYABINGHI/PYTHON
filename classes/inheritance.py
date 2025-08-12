# inheritance.py
# inheritance.py
# This file demonstrates the use of inheritance in Python classes.

class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"This is a shape named {self.name}")

shape1 = Shape(name="Circle")
shape1.describe()
shape2 = Shape(name="Square")
shape2.describe()
shape3 = Shape(name="Triangle")
shape3.describe()
shape4 = Shape(name="Rectangle")
shape4.describe()
shape5 = Shape(name="Pentagon")
shape5.describe()
shape6 = Shape(name="Hexagon")
shape6.describe()
shape7 = Shape(name="Octagon")
shape7.describe()

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(name="Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

Rectangle1 = Rectangle(length=5, width=3)
print(f"Area of {Rectangle1.name}: {Rectangle1.area()}")
print(f"Perimeter of {Rectangle1.name}: {Rectangle1.perimeter()}")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(name="Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

Circle1 = Circle(radius=4)
print(f"Area of {Circle1.name}: {Circle1.area()}")
print(f"Circumference of {Circle1.name}: {Circle1.circumference()}")
