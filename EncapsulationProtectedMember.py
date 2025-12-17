class Car:
    def __init__(self):
        self.speed = 120

class SportsCar(Car):
    def show_speed(self):
        print("Speed:", self.speed)

car = SportsCar()
car.show_speed()
print(car.speed)