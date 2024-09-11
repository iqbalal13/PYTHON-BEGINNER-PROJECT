import math

while True:
    print("Choose a 3D shape:")
    print("1. Sphere")
    print("2. Cube")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Exit")

    choice = int(input("Enter the number corresponding to your choice: "))

    if choice == 5:
        print("Exiting the program. Goodbye!")
        break

    if choice == 1:
        radius = float(input("Enter the radius of the sphere: "))
        print("Volume of the sphere:", (4/3) * math.pi * radius**3)
    elif choice == 2:
        side_length = float(input("Enter the side length of the cube: "))
        print("Volume of the cube:", side_length**3)
    elif choice == 3:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        print("Volume of the cylinder:", math.pi * radius**2 * height)
    elif choice == 4:
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        print("Volume of the cone:", (1/3) * math.pi * radius**2 * height)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")