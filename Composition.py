class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self,engine):
        self.engine = engine
    def start_car(self):
        self.engine.start()
    def drive(self):
        self.engine.start()
        print("Car is Driving")
class ElectricEngine:
    def start(self):
        print("Electric Engine Started")
class DieselEngine:
    def start(self):
        print("Diesel Engine Started")
class PetrolEngine:
    def start(self):
        print("Petrol Engine Started")
engine = PetrolEngine()
car = Car(engine)
car.start_car()