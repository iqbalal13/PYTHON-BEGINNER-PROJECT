import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def cube_volume(side_length):
    return side_length**3

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

def main():
    print("Choose a 3D shape:")
    print("1. Sphere")
    print("2. Cube")
    print("3. Cylinder")
    print("4. Cone")

    choice = int(input("Enter the number corresponding to your choice: "))

    if choice == 1:
        radius = float(input("Enter the radius of the sphere: "))
        print("Volume of the sphere:", sphere_volume(radius))
    elif choice == 2:
        side_length = float(input("Enter the side length of the cube: "))
        print("Volume of the cube:", cube_volume(side_length))
    elif choice == 3:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        print("Volume of the cylinder:", cylinder_volume(radius, height))
    elif choice == 4:
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        print("Volume of the cone:", cone_volume(radius, height))
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()