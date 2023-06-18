from Shape import Shape
from Rhombus import Rhombus
from Circle import Circle
from Ellipse import Ellipse


def load(file_name):
    print(f"Processing {file_name} ...")
    print()

    try:
        with open(file_name, "r") as file:
            shapes = []
            shapes_count = 0
            circles_count = 0
            rhombus_count = 0
            ellipse_count = 0
            invalid_count = 0

            for line_num, line in enumerate(file, start=1):
                split_shape_array = line.split()

                if split_shape_array[0] not in ["ellipse", "circle", "rhombus", "shape"]:
                    print("Invalid shape type on line", line_num, ", please check for typos")
                    invalid_count += 1
                    continue

                try:
                    if split_shape_array[0] == "shape":
                        shape_object = Shape()
                        shapes_count += 1
                    elif split_shape_array[0] == "rhombus":
                        shape_object = Rhombus(float(split_shape_array[1]), float(split_shape_array[2]))
                        rhombus_count += 1
                    elif split_shape_array[0] == "circle":
                        shape_object = Circle(float(split_shape_array[1]))
                        circles_count += 1
                    elif split_shape_array[0] == "ellipse":
                        shape_object = Ellipse(float(split_shape_array[1]), float(split_shape_array[2]))
                        ellipse_count += 1
                except (IndexError, ValueError):
                    print("Error: Invalid shape data on line", line_num)
                    invalid_count += 1
                    continue

                shapes.append(shape_object)

            total = len(shapes)
            print()
            print("Total processed rows:", total)
            print("Shapes:", shapes_count)
            print("Circles:", circles_count)
            print("Rhombus:", rhombus_count)
            print("Ellipse:", ellipse_count)
            print("Invalid / Error:", invalid_count)
            print()

            return shapes

    except (FileNotFoundError, PermissionError):
        print("Invalid path or file not found or no permission for access, system is shutting down")
        exit()


def to_set(multiset):
    return set(multiset)


def save(input_list, path):
    try:
        with open(path, "w") as file:
            for item in input_list:
                file.write(item.print_info() + "\n")
    except IOError:
        print("Error writing to file.")


def object_printer(shapes_set):
    for shape in shapes_set:
        print(shape.print_info())
        print()


def summary(input_list):
    shapes_count = len(input_list)
    circles_count = sum(isinstance(shape, Circle) for shape in input_list)
    rhombus_count = sum(isinstance(shape, Rhombus) for shape in input_list)
    ellipse_count = sum(isinstance(shape, Ellipse) for shape in input_list)

    print("SUMMARY:")
    print("Circle(s) :", circles_count)
    print("Ellipse   :", ellipse_count)
    print("Rhombus   :", rhombus_count)
    print("Shape     :", shapes_count)
    print()


def details(input_list):
    for item in input_list:
        print(item.get_details())


def quit_program():
    exit()
