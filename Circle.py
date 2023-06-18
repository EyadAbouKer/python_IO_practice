import math
from Shape import Shape

class Circle(Shape):
    def __init__(self, radius=0):
        super().__init__()
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def print_info(self):
        return f"This {self.__class__.__name__} has id={self.id}, perimeter={self.calculate_perimeter()}, area={self.calculate_area()}"

    def __hash__(self):
        return hash(self.radius)

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def get_details(self):
        return f"Circle with radius: {self.radius}"
