# initializer
# special method in a class that is called when an instance of the class is created
# it is used to initialize the attributes of the class

class Human():

    def __init__(self,gender,name):
        print("The initializer wass called")
        
        self.gender=gender
        self.name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"

    def another_one(self):
        print("This is another method")
    
adam=Human(name="adam",gender="Male") #object from a class
print("name",adam.name)
print("gender",adam.gender)
print("ribs",adam.ribs)
print("ribs",adam.curse)
print("")
eve=Human(name="eve",gender="Female")
print("name",eve.name)
print("gender",eve.gender)
print("ribs",eve.ribs)
print("curse",eve.curse)