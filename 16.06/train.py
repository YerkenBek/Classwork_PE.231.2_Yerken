from random import randint

class Train:
    source = ""
    destination = ""
    number = 0

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.number = randint(100, 999)

    def board(self, person):
        if person.ticket:
            if self.source == person.ticket.source and self.destination == person.ticket.destination:
                msg = "Welcome on board %s, Your train #%s arrived, from %s to %s." % (person.name, self.number,
                                                    self.source, self.destination)
                print(msg)
                person.ticket = None
            else:
                print("Wrong ticket number")
        else:
            print("No tickets")

    def show(self):
        msg = "Train #%s, from station %s to station %s." % (self.number, self.source, self.destination)
        print(msg)