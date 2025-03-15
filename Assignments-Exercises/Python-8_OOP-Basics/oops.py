# define the car class
class Car:
    # constructor method to initialize the object
    def __init__(carself, make, model, year):
        carself.make = make
        carself.model = model
        carself.year = year

    # method to return a description of the car
    def describe(carself):
        return f"This car is a {carself.year} {carself.make} {carself.model}."
    
# create an instance of the car class
my_car = Car("Tuyota", "Coroya", 2025)

# print the description of the car
print(my_car.describe())

# create another instance of the car class
my_car = Car("Telsa", "musk", 2025)

# print the description of the car
print(my_car.describe())