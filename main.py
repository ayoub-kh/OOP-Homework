#Python class Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class rectangle:
    def __init__(self,lenght,width):
       self.lenght = lenght
       self.width = width

    def area(self):
        return self.lenght*self.width

a= rectangle(10,10)
print(a.area())

#Vehicle class with max_speed and mileage instance attributes
class Vehicule:
    def __init__(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

#Vehicle class without any variables and methods.
class Vehicule:
    pass

#child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicule):
    pass

b= Bus("bus",125,"test")
print(b.max_speed)