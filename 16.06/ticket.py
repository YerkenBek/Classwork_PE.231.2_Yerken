from random import randint

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