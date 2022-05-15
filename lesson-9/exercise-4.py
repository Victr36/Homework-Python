class Car:
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0

    def go(self, speed=35):
        self.speed = speed
        print(f"Car model {self.name} go, speed {self.speed}.")

    def stop(self):
        self.speed = 0
        print(f"Car model {self.name} stop.")

    def turn(self, direction):
        if direction == "left" or direction == "right":
            print(f"Car model {self.name} turn on the {direction}")
        else:
            print(f"Car programming turn on the left and on the right")

    def show_speed(self):
        print(f"Speed car {self.speed}")


class TownCar(Car):

    def show_speed(self):
        if self.speed >=61:
            print(f"Your speed {self.speed},")
        else:
            print(f"Speed car {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed >=41:
            print(f"Your speed {self.speed}")
        else:
            print(f"Speed car {self.speed}")


class PoliceCar(Car):
    is_police = True


auto_1 = PoliceCar("blue", "Lada")
auto_1.go(20)
auto_2 = SportCar("red", "Mersedes")
auto_2.go(80)
auto_2.show_speed()
auto_2.turn("right")
auto_3 = WorkCar("black", "JCB")
auto_3.go(46)
auto_3.show_speed()
auto_4 = TownCar("white", "Lada")
auto_4.go(64)
auto_4.show_speed()
auto_4.stop()
auto_4.show_speed()
