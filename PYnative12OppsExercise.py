#1 Write a Python program to create a Vehicle class with 
# max_speed and mileage instance attributes.
'''
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed =max_speed
        self.mileage = mileage

model = Vehicle(240,18)
print("Car Mileage is :",model.mileage)
print("Car Max speed is: ", model.max_speed)

'''
#2
'''
class Vehicle:
    pass
'''
#3
'''
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed =max_speed
        self.mileage = mileage

class bus(Vehicle):
    pass

school_bus = bus(240,18)
print(school_bus.max_speed,school_bus.mileage)
'''

#4
'''
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    
school_bus = Bus("School Volvo " ,180,12)
print(school_bus.seating_capacity())

'''

#5 
'''
class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo" ,180,12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

'''
#6
'''
class Vehicle:
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity *100
    
class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount
    
School_bus = Bus("School Volvo" ,12,50)
print("Total Bus Fare is: ",School_bus.fare())

'''

#7

















































