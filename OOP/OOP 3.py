class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")

    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopping.")

my_car = Car("Honda", "Civic", 2021)

my_car.start()
my_car.stop()