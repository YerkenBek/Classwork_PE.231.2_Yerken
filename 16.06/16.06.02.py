from random import randint

class Person:
    balance = 0
    name = ""
    iin = 0
    age = 0
    ticket = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.iin = randint(100000000000, 999999999999)
    
    def show(self):
        msg = "Person %s, age %s years, IIN: %s. Money: %s" % (self.name, 
                self.age, self.iin, self.balance)
        print(msg)

    def earn(self, amount):
        self.balance += amount

    def pay(self, amount):
        if self.balance < amount:
            return 0
        self.balance -= amount
        return amount

class Ticket:
    number = 0
    passenger_name = ""
    passenger_iin = 0
    passenger_age = 0
    source = ""
    destination = ""

    def __init__(self, source, destination, pas_name, pas_iin, pass_age):
        self.number = randint(100000, 999999)
        self.source = source
        self.destination = destination
        self.passenger_name = pas_name
        self.passenger_iin = pas_iin
        self.passenger_age = pass_age

    def show(self):
        msg = "Ticket #%s: %s -- %s" %(self.number, self.source, self.destination)
        msg += "  Passenger: %s, %s years old, IIN: %s " % (self.passenger_name, 
                                    self.passenger_age, self.passenger_iin)
        print(msg)    

class Kassa:
    balance = 0

    def get_price(self, source, destination):
        return (len(source) + len(destination) * 1000)
    


test_man = Person("Ilon Mask", 56)
test_man.earn(25000)
test_man.pay(12931)
test_man.show()

test_ticket = Ticket("Almaty", "Santiago", test_man.name, test_man.iin, test_man.age)
test_ticket.show()

kassa = Kassa()
price = kassa.get_price("Almaty", "Santiago")
print(price)
