class Shapes():
    # CLASS OBJECT ATTRIBUTES
    Type = "Mammal"

    def __init__(self, colour):
        self.colour = colour

    def what_am_i(self):
        return "I am a shape"

    def change_colour(self, colour):
        self.colour = colour


MyShape = Shapes('Red')
print(MyShape.colour)

# ------------
# Inheritance

class Circle(Shapes):
    def __init__(self, radius, colour):
        Shapes.__init__(self, colour)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

MyCircle = Circle(3, 'Blue')
print(MyCircle.colour)
print(MyCircle.radius)
print(MyCircle.area())
print(MyCircle.perimeter())
print(MyCircle.what_am_i())