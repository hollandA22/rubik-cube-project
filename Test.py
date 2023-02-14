import tkinter as tk
import math

class Cube3D:
    def __init__(self, master, size):
        self.master = master
        self.canvas = tk.Canvas(master, width=size, height=size, bg="white")
        self.canvas.pack()

        # Define the 3D coordinates of each vertex of the cube
        self.vertices = [[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0],
                         [0, 0, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]]

        # Define the edges of the cube
        self.edges = [[0, 1], [1, 2], [2, 3], [3, 0],
                      [4, 5], [5, 6], [6, 7], [7, 4],
                      [0, 4], [1, 5], [2, 6], [3, 7]]

        # Initialize the mouse position and rotation angles
        self.last_x, self.last_y = None, None
        self.theta, self.phi = 0, 0

        # Bind mouse events to the canvas
        self.canvas.bind("<Button-1>", self.on_left_mouse_down)
        self.canvas.bind("<ButtonRelease-1>", self.on_left_mouse_up)
        self.canvas.bind("<B1-Motion>", self.on_left_mouse_drag)

        self.update()

    def draw_cube(self):
        # Project the 3D coordinates onto the 2D canvas
        points = []
        for vertex in self.vertices:
            x = vertex[0] * 100 + 150
            y = vertex[1] * 100 + 150
            z = vertex[2] * 100 + 150
            x, y = self.rotate_point(x, y, z)
            points.append((x, y))

        # Draw the edges of the cube
        for edge in self.edges:
            x1, y1 = points[edge[0]]
            x2, y2 = points[edge[1]]
            self.canvas.create_line(x1, y1, x2, y2)

    def on_left_mouse_down(self, event):
        self.last_x, self.last_y = event.x, event.y

    def on_left_mouse_up(self, event):
        self.last_x, self.last_y = None, None

    def on_left_mouse_drag(self, event):
        if self.last_x is not None and self.last_y is not None:
            dx = event.x - self.last_x
            dy = event.y - self.last_y
            self.rotate_cube(dx, dy)
            self.canvas.delete("all")
            self.draw_cube()
        self.last_x, self.last_y = event.x, event.y

    def rotate_cube(self, dx, dy):
        self.theta += dx / 10
        self.phi -= dy / 10

    def rotate_point(self, x, y, z):
        # Rotate the point around the x, y, and z axes
        x1 = x * math.cos(self.theta) - y * math.sin(self.theta)
        y1 = y * math.cos(self.theta) + x * math.sin(self.theta)
        z1 = z

        x2 = x1
        y2 = y1 * math.cos(self.phi) - z1 * math.sin(self.phi)
        z2 = z1 * math.cos(self.phi) + y1 * math.sin(self.phi)

        return x2, y2

    def update(self):
        # Rotate the cube a small amount
        self.canvas.delete("all")
        self.draw_cube()
        self.master.after(50, self.update)

root = tk.Tk()
root.title("3D Cube")

cube = Cube3D(root, size=400)

root.mainloop()
