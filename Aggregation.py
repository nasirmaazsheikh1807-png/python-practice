class Driver:
    def __init__(self,name):
        self.name = name

class Car:
    def __init__(self,driver):
        self.driver = driver
    def show_driver(self):
        print(f"Driver: {self.driver.name}")
driver = Driver("Rahul")
car = Car(driver)
car.show_driver()