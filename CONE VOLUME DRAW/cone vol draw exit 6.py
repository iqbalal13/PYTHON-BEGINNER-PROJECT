import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def draw_cone(radius, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create points for the base circle
    theta = np.linspace(0, 2*np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Plot the base circle
    ax.plot(x, y, zs=0, zdir='z', label='Base Circle')

    # Plot lines from the base to the apex
    ax.plot([0], [0], [0], 'ro')  # Apex point
    ax.plot(x, y, zs=height, zdir='z', label='Slant Lines')

    # Connect the base circle to the apex using a while loop
    i = 0
    while i < len(theta):
        ax.plot([x[i], 0], [y[i], 0], [0, height], color='black')
        i += 1

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Cone')

    plt.show()

# Main program using a for loop
for _ in range(100):  # Adjust the number of iterations as needed
    print("\nOptions:")
    print("1. Calculate cone volume and draw")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))

        draw_cone(radius, height)

    elif choice == "2":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 or 2.")