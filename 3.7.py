class Car:
    def __init__(self, model, year, power, price, mileage, circles = 4):
        self.model = model
        self.year = year
        self.power = power
        self.price = price
        self.mileage = mileage
        self.circles = circles

    def description(self):
        print(f"{self.model,self.year,self.power,self.price, self.mileage, self.circles}")

class Truck (Car):
    def __init__(self, model, year, power, price, mileage):
        super().__init__(model,year,power,price,mileage)
        self.circles = 8

car1 = Car("LADA", 1985, 253, 2500000, 40000000, 4)
car2 = Truck("Truck", 1999, 100, 15000, 31834534)

car1.description()
car2.description()