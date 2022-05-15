class Stationery:
    def __init__(self, title="something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawning! {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Start drawning with {self.title} pen!")

class Pencil(Stationery):
    def draw(self):
        print(f"Start drawning with {self.title} pencil!")

class Marker(Stationery):
    def draw(self):
        print(f"Start drawning with {self.title} marker!")


stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
marker = Marker("COPIC")
marker.draw()
