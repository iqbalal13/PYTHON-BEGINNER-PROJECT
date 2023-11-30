def calculate_cube_volume(side_length):
    volume = side_length ** 3
    return volume

def calculate_rectangular_prism_volume(length, width, height):
    volume = length * width * height
    return volume

def main():
    while True:
        print("Welcome to the 3D Volume Calculator!")
        print("Choose an option:")
        print("1. Calculate the volume of a cube")
        print("2. Calculate the volume of a rectangular prism")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            side_length = float(input("Enter the side length of the cube in feet: "))
            cube_volume = calculate_cube_volume(side_length)
            print(f"The volume of the cube is {cube_volume} cubic feet.")

        elif choice == "2":
            length = float(input("Enter the length of the rectangular prism in feet: "))
            width = float(input("Enter the width of the rectangular prism in feet: "))
            height = float(input("Enter the height of the rectangular prism in feet: "))
            prism_volume = calculate_rectangular_prism_volume(length, width, height)
            print(f"The volume of the rectangular prism is {prism_volume} cubic feet.")

        elif choice == "3":
            print("Exiting the 3D Volume Calculator. Goodbye!")
            break  # Exit the while loop

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()