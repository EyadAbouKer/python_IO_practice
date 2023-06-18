import math
from Shape import Shape

class Rhombus(Shape):
    def __init__(self, diagonal1=0, diagonal2=0):
        super().__init__()
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def calculate_perimeter(self):
        return 2 * (self.diagonal1 + self.diagonal2)

    def calculate_area(self):
        return (self.diagonal1 * self.diagonal2) / 2

    def calculate_side(self):
        return math.sqrt(self.diagonal1 ** 2 + self.diagonal2 ** 2) / 2

    def calculate_inradius(self):
        if 2 * math.sqrt(self.diagonal1 ** 2 + self.diagonal2 ** 2) == 0:
            return None
        else:
            return (self.diagonal1 * self.diagonal2) / (2 * math.sqrt(self.diagonal1 ** 2 + self.diagonal2 ** 2))

    def print_info(self):
        return f"This {self.__class__.__name__} has id={self.id}, diagonal1={self.diagonal1}, diagonal2={self.diagonal2}, area={self.calculate_area()}, side={self.calculate_side()}, and inradius={self.calculate_inradius()}"

    def __hash__(self):
        return hash((self.diagonal1, self.diagonal2))

    def __eq__(self, other):
        if isinstance(other, Rhombus):
            return self.diagonal1 == other.diagonal1 and self.diagonal2 == other.diagonal2
        return False

    def get_details(self):
        return f"Rhombus with diagonal1: {self.diagonal1}, diagonal2: {self.diagonal2}"
