class Kettle():
    material = "steel"
    color = "red"
    volume = 2.4
    water = 0

    def fill(self, liters):
        self.water += liters
        print("Now in kettle", {self.water}, "l")

my_kettle = Kettle()
my_kettle.fill(2)

other_kettle = Kettle()
my_kettle.color = "blue"

Kettle_color = "red"

print(my_kettle.color, other_kettle.color )

my_kettle.fill(2)
print(my_kettle.water)
