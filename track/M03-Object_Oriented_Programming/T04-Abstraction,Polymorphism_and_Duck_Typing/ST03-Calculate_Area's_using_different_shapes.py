class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        # Write your code here
        return length * breadth


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        # Write your code here
        return side * side


length = int(input())
breadth = int(input())
side = int(input())

shapes = [Rectangle(length, breadth), Square(side)]

for shape in shapes:
    print(shape.area())