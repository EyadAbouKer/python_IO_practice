from methods import *


def main():
    shapes = []

    while True:
        print("************************** SHAPE PROCESSING MENU ******************************")
        print("1. Load Shapes")
        print("2. Print Shapes")
        print("3. Print Summary")
        print("4. Print Details")
        print("5. Save Shapes")
        print("6. Convert to Set")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            file_name = input("Enter the file name: ")
            shapes = load(file_name)
            print("Shapes loaded successfully.")
        elif choice == "2":
            object_printer(shapes)
        elif choice == "3":
            summary(shapes)
        elif choice == "4":
            details(shapes)
        elif choice == "5":
            path = input("Enter the file path to save shapes: ")
            save(shapes, path)
            print("Shapes saved to file.")
        elif choice == "6":
            shapes_set = to_set(shapes)
            object_printer(shapes_set)
            print("Shapes converted to a set.")
        elif choice == "7":
            quit_program()
        else:
            print("Invalid choice. Please try again.")

        print()  # Add a line break for readability


if __name__ == "__main__":
    main()
