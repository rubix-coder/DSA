class CreditCard:
    def __init__(self, customer,bank,acnt,limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_limit(self):
        return self._limit

    def get_account(self):
        return self._acnt

    def get_balance(self):
        return self._balance

    def charge(self,price):
        if self._balance + price > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,amount):
        self._balance -= amount

    def get_all(self):
        print(f"All details\n{self._customer},{self._bank},{self._acnt},{self._balance}")

    def __add__(self,nam):
        print (f"Hello {nam}, this is operator overloading and polymorphism")

    def __repr__(self):
        print("This is representation")

    def __str__(self):
        print("This is str present")
        range
