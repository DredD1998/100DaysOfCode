def calculate(n,**kwargs):
    print(n,kwargs)
    for key,value in kwargs.items():
        print(f"{key} : {value}")



calculate(6,add=3,multiply=5,divide=2,subtract=1)




class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

# my_car = Car(make="Nissan",model="GT-R")
my_car = Car(model="GT-R")

print(my_car.make)
print(my_car.model)