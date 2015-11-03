# coding: utf-8

def test(speed):
    
    if speed < 0:
        print ("Вы ошиблись, скорость не может быть меньше 0")

class Tank:

    carriage = True
    track = True

    def __init__(self, model=None, speed=0):
        self.model = model
        self.speed = speed
        test(speed)

    def status(self):
        print ("Танк", self.model, "едет со скоростью", self.speed, "шасси?", self.carriage, "гусеницы?", self.track)


class Car:

    wheel = 4

    def __init__(self, model=None, speed=0):
        self.model = model
        self.speed = speed
        test(speed)

    def status(self):
        if self.wheel > 4:
            print ("Грузовик", self.model, "едет со скоростью", self.speed, self.wheel, "колес")
        elif self.wheel < 3:
            print ("У машины не может быть менее 3 колес")
        else:
            print ("Машина", self.model, "едет со скоростью", self.speed, self.wheel, "колеса")

class Cart:

    wheel = 4

    def __init__(self, model=None, speed=0):
        self.model = model
        self.speed = speed
        test(speed)

    def status (self):
        if self.wheel < 1:
            print ("Телега не поедет без колес")
        else:
            print ("Телега", self.model, "едет со скоростью", self.speed, self.wheel, "колес")


t34 = Tank(model='T34', speed=100)
audi = Car(model='Audi', speed=100)
trolley = Cart(model='Trolley', speed=50)

cars = [t34, audi, trolley]

t34.carriage = False
audi.speed = 90
trolley.wheel = 3

for car in cars:
    car.status()
