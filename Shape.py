class Shape:
    current_id = 0

    def __init__(self):
        Shape.current_id += 1
        self.id = Shape.current_id
        self.perimeter = "undefined"
        self.area = "undefined"


    def print_info(self):
        return f"This {self.__class__.__name__} has id={self.id}, perimeter={self.perimeter}, area={self.area}"

    def calculate_perimeter(self):
        return None

    def calculate_area(self):
        return None

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Shape):
            return False

    def get_details(self):
        return f"Shape name: shape"
