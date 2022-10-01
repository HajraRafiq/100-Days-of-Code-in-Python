class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale , Exhale.")
    
# Introducing a new Fish class and Inheriting the functions and behavior from Animal Class

class Fish(Animal):
    def __init__(self):
        super().__init__()  #super keyword is used to inherit everything from Animal CLass
    def swim(self):
        print("Moving in Water")

    def breathe(self):
        super().breathe() # Inheriting breathe function from Animal Class and adding another behavior for Fish
        print("Doing this underwater")

nemo = Fish()
nemo.breathe()
nemo.swim()