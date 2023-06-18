import math
from Shape import Shape

class Ellipse(Shape):
    def __init__(self, semi_major=0, semi_minor=0):
        super().__init__()
        if isinstance(semi_major, (int, float)) and isinstance(semi_minor, (int, float)):
            self.semi_major = max(semi_major, semi_minor)
            self.semi_minor = min(semi_major, semi_minor)
        else:
            raise ValueError("Invalid input. Please enter valid numbers.")

    def calculate_area(self):
        if self.semi_minor < 0 or self.semi_major < 0:
            print("Warning: One of the perimeters of the ellipse is less than zero.")
        area = math.pi * self.semi_minor * self.semi_major
        return area

    def calculate_eccentricity(self):
        if self.semi_major < 0 or self.semi_minor < 0:
            print("Invalid shape: negative input.")
            return None
        else:
            return math.sqrt(abs(self.semi_minor ** 2 - self.semi_major ** 2))

    def print_info(self):
        return f"This {self.__class__.__name__} has id={self.id}, semi-major={self.semi_major}, semi-minor={self.semi_minor}, area={self.calculate_area()}, eccentricity={self.calculate_eccentricity()}"

    def __hash__(self):
        return hash((self.semi_major, self.semi_minor))

    def __eq__(self, other):
        if isinstance(other, Ellipse):
            return self.semi_major == other.semi_major and self.semi_minor == other.semi_minor
        return False

    def get_details(self):
        return f"Ellipse with semi-major axis: {self.semi_major}, semi-minor axis: {self.semi_minor}"
