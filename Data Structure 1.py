#creating a class

class Fruit:
    #making a constructor with attributes
    def __init__(self, taste, colour, smell, preference):
        self.taste = taste
        self.colour = colour
        self.smell = smell
        self.preference = preference

    #getter method
    def get_taste(self):
        return self.taste
        
     #setter method
    def set_colour(self, new_colour):
        self.colour=new_colour
        
    #custom method
    def showFruit(self):
        print("Hello, i am a fruit {} {} {} {}".format(self.taste, self.colour, self.smell, self.preference))

apple=Fruit("sweet sour","red","sweet",2)
print(apple.get_taste())
apple.set_colour("orange")
apple.showFruit()
