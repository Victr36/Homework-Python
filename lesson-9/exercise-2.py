class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass_calculation(self, weight=25, thickness=5):
        return f'Масса асфальта: {(self.length * self.width * weight * thickness) / 1000} т'

road_1 = Road(5000, 20)
print(road_1.mass_calculation())
