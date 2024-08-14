#Inheritance -  Having a child class with all properties of parent class along with its own properties
#Child class has been inherited from the parent class

#parent class
class Car:
    #constructor
    def __init__(self,brand,model,colour):
        self.brand=brand
        self.model=model
        self.colour=colour

    #getter methods
    def get_model(self):
        return self.model
    
    #setter method
    def set_colour(self,new_colour):
        self.colour=new_colour

    #custom method
    def showCar(self):
        print("This is a {} car made by {} and is this colour {}".format(self.model,self.brand,self.colour))

#child class
class SUV(Car):
    def __init__(self, brand, model, colour, seats):
        Car.__init__(self,brand,model,colour)
        self.seats=seats

Audi=SUV("Audi","Q3","Black","5")
Audi.showCar()

Audi.set_colour("Navy")
Audi.showCar