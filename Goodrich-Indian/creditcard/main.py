from creditcard import CreditCard
from predatorycreditcard import PredatoryCreditCard

if __name__=="__main__":
    cc = CreditCard("Jesal","HDF","12345678",900)
    cc.get_all()
    cc.charge(100)
    cc.make_payment(32)
    cc.get_all()
    cc+['anme']
    cc = PredatoryCreditCard("Jesal","HDF","12345678",900,50)
    cc.charge(4)
    