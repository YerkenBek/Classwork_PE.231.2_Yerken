usage
class Dog:
    type = ""
    size = 0
    color = ""
    def __init__(self, type, size, color):
        self.type = type
        self.size = size
        size.color = color

    usage
    def bark(self):
        print("Gav-gav!")
        print(self.color)

my_little_dog = Dog("foxterier", 20, "white")
my_little_dog.bark()
