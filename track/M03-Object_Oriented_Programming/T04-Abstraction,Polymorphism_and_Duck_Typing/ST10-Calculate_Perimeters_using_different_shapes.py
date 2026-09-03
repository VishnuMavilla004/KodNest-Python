class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        # Write your code here
        Perimeter = 2*(self.length + self.breadth)
        return Perimeter


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        # Write your code here
        Perimeter_of_Square = 4*(self.side)
        return Perimeter_of_Square


length = int(input())
breadth = int(input())
side = int(input())

shapes = [Rectangle(length, breadth), Square(side)]

for shape in shapes:
    print(shape.perimeter())