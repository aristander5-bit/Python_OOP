import tkinter as tk
from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def draw(self, canvas: tk.Canvas):
        pass

class Circle(Graphic):
    def __init__(self, x: int, y: int, radius: int, color: str = "blue"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, canvas: tk.Canvas):
        x1 = self.x - self.radius
        y1 = self.y - self.radius
        x2 = self.x + self.radius
        y2 = self.y + self.radius
        canvas.create_oval(x1, y1, x2, y2, outline=self.color, width=2)


class Square(Graphic):
    def __init__(self, x: int, y: int, size: int, color: str = "red"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, canvas: tk.Canvas):
        canvas.create_rectangle(
            self.x, self.y,
            self.x + self.size, self.y + self.size,
            outline=self.color, width=2
        )

class Line(Graphic):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, color: str = "black"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def draw(self, canvas: tk.Canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color, width=2)


class CompositeGraphic(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic: Graphic):
        self.children.append(graphic)

    def remove(self, graphic: Graphic):
        self.children.remove(graphic)

    def draw(self, canvas: tk.Canvas):
        for child in self.children:
            child.draw(canvas)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Python CAD - Composite Pattern")
    canvas = tk.Canvas(root, width=500, height=400, bg="white")
    canvas.pack()

    wall = Square(150, 150, 200, color="black")
    window = Square(180, 180, 50, color="blue")
    sun = Circle(400, 70, 35, color="orange")
    roof_left = Line(150, 150, 250, 70, color="brown")
    roof_right = Line(250, 70, 350, 150, color="brown")

    roof = CompositeGraphic()
    roof.add(roof_left)
    roof.add(roof_right)

    main_drawing = CompositeGraphic()
    main_drawing.add(wall)
    main_drawing.add(window)
    main_drawing.add(sun)
    main_drawing.add(roof)

    main_drawing.draw(canvas)

    root.mainloop()