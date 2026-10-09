class car:
    def __init__(self):
        self.color="black"
    def protect(self):
        print("car protect us")
    @staticmethod
    def travel():
        print("we travel in car")
    @classmethod
    def mileage(cls):
        print("car gives us mileage")
c1=car()
c1.protect()
c1.travel() # not standard way to declare
c1.mileage()  # not standard way to declare
car.travel() # standard way to declare
car.mileage()  # standard way to declare
car.protect() # error


