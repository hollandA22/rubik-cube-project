import tkinter as tk

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

        # Draw the cube
        self.draw_cube()

        # Initialize the mouse position and rotation angles
        self.last_x, self.last_y = None, None
        self.theta, self.phi = 0, 0

        # Bind mouse events to the canvas
        self.canvas.bind("<Button-1>", self.on_left_mouse_down)
        self.canvas.bind("<ButtonRelease-1>", self.on_left_mouse_up)
        self.canvas.bind("<B1-Motion>", self.on_left_mouse_drag)

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