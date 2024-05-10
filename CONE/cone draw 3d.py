import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_cone(radius, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create the parametric circle for the base
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = radius * np.cos(theta)
    y_circle = radius * np.sin(theta)

    # Plot the base circle
    ax.plot(x_circle, y_circle, zs=0, zdir='z', color='b')

    # Plot the lines connecting the top to the base
    ax.plot([0]*len(theta), [0]*len(theta), zs=height, zdir='z', color='b')
    ax.plot_surface([x_circle, x_circle], [y_circle, y_circle], [0, height], color='b', alpha=0.5)

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Set the radius and height of the cone
cone_radius = 5
cone_height = 10

# Call the function to plot the 3D cone
plot_3d_cone(cone_radius, cone_height)