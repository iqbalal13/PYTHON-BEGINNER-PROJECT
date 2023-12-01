import math

print("3D Shape Volume Calculator")

print("Choose a 3D shape:")
print("1. Sphere")
print("2. Cube")
print("3. Cylinder")
print("4. Cone")
print("5. Exit")

choice = int(input("Enter the number corresponding to your choice: "))

if choice == 1:
    radius = float(input("Enter the radius of the sphere: "))
    volume = (4/3) * math.pi * radius**3
    print("Volume of the sphere:", volume)
elif choice == 2:
    side_length = float(input("Enter the side length of the cube: "))
    volume = side_length**3
    print("Volume of the cube:", volume)
elif choice == 3:
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = math.pi * radius**2 * height
    print("Volume of the cylinder:", volume)
elif choice == 4:
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    volume = (1/3) * math.pi * radius**2 * height
    print("Volume of the cone:", volume)
elif choice == 5:
    print("Exiting the program. Goodbye!")
else:
    print("Invalid choice. Please enter a number between 1 and 5")