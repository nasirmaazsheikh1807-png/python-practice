class Car:
    wheels = 4 #Class Attribute
    def __init__(self,brand,model): #object 
        self.brand = brand   #instance attribute
        self.model = model   #Instance Attribute
    def start(self):             #Method
        print(self)
        print(self.brand,self.model,"is starting")

car = Car("Toyota","Fortuner")
car1 = Car("BMW","M4")
# car1.wheels = 6
# print(car1.brand)
# print(car.brand)
# print(car.wheels)
# print(car1.wheels)
car.start()