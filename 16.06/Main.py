from kassa import Kassa
from person import Person
from ticket import Ticket
from train import Train

test_man = Person("Ilon Mask", 56)
test_man.earn(25000)
test_man.pay(12931)
test_man.show()

#test_ticket = Ticket("Almaty", "Santiago", test_man.name, test_man.iin, test_man.age)
#test_ticket.show()

kassa = Kassa()
price = kassa.get_price("Almaty", "Santiago")
kassa.buy_ticket("Almaty", "Santiago", test_man)

if test_man.ticket:
    test_man.ticket.show()

train = Train("Almaty", "Santiago")
train.show()

train.board(test_man)
if test_man.ticket is None:
    print("Ticket is over")
