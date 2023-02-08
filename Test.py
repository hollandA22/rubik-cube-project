import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_rubiks_cube(front, back, up, down, left, right):
    """
    Plot a 3x3 Rubik's cube using 6 lists for each side.
    Each list should contain 9 elements, representing the color of each square.
    """
    # Combine the 6 lists into a single 3D array
    cube = np.zeros((3, 3, 6))
    cube[:, :, 0] = front.reshape((3, 3))
    cube[:, :, 1] = back.reshape((3, 3))
    cube[:, :, 2] = up.reshape((3, 3))
    cube[:, :, 3] = down.reshape((3, 3))
    cube[:, :, 4] = left.reshape((3, 3))
    cube[:, :, 5] = right.reshape((3, 3))
    
    # Define the x, y, and z coordinates for each face of the cube
    x = np.array([0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0])
    y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])
    z = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])

    # Define the colors for each face
    colors = np.zeros((16, 4))
    colors[:, :3] = cube[x, y, z]
    colors[:, 3] = 1

    # Plot the cube
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_zlim(0, 3)
    ax.set_xticks(np.arange(0, 4))
    ax.set_yticks(np.arange(0, 4))
    ax.set_zticks(np.arange(0, 4))
    ax.voxels(cube, facecolors=colors, edgecolor='k')
    plt.show()
