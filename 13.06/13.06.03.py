class Kettle():
    temperature = ""
    material = ""
    color = ""
    volume = 2.4
    water = 0

    def __init__ (self, material, color, volume):
        self.material = material
        self.color = color
        self.volume = volume

    def fill(self, liters):
        self.water += liters
        if self.water > self.volume:
            extra = self.water - self.volume
            print("out extra water")
            self.water = self.volume 
        print(f"now in kettle {self.water} l")
    
    def pour(self, liters):
        if liters > self.water:
            print(f"cannot spill more water than {self.water} l")

        else:
            self.water -= liters
        print(f"now in kettle {self.water} l")

    def boil(self):
        self.temperature = 100
        print("Wheeeeeeeeeeeeeeeeee!!")


my_kettle = Kettle("bamboo", "brown", 5)
my_kettle.fill(3)

Kettle.color = "black"
print(my_kettle.color)

my_kettle.pour(2)
my_kettle.boil()
