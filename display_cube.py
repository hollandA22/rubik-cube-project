import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import proj3d

def rotate_polygon(polygon, angle, axis):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])
    return np.dot(polygon, rotation_matrix)

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Defining verticies of the cube
    vertices = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[1,1,1],[0,1,1]])

    # Defining the faces of the cube as polygon collections
    x, y, z = zip(*vertices)

    # Defining each face as a 3D polygon
    polygons = [[1, 5, 7, 3], [0, 4, 6, 2], [0, 1, 5, 4], [2, 6, 7, 3], [0, 2, 3, 1], [4, 5, 7, 6]]
    """
    polygons = [[vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[0], vertices[3], vertices[7], vertices[4]]]
    """
    # Defining colors for each face
    colors = ['red','blue','orange','white','yellow','green']

    # Transform cube durring rotation
    angle = np.pi / 4
    axis = [1, 1, 0]
    polygons[0] = rotate_polygon(vertices[polygons[0]], angle, axis)

    # Adding each face to the plot
    for i in range(len(polygons)):
        ax.add_collection(Poly3DCollection([polygons[i]], facecolors=colors[i]))

    # Set plot properties
    ax.set_xlim3d(-1, 2)
    ax.set_ylim3d(-1, 2)
    ax.set_zlim3d(-1, 2)

    # Remove axes labels and tick marks
    ax.set_axis_off()

    

    # Display plot
    plt.show()

main()