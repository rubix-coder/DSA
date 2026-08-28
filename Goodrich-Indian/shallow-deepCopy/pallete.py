class _:
    def __init__(self,text):
        self.__txt = text

    def __name__(self):
        return str("patel")

    def __str__(self):
        " ".join(self.__txt)
        return str(_.__name__ + " ".join(self.__txt))

jp  = _("jesal")
print(jp)
print(_.__qualname__)        # the class's actual dotted name
print(type(jp).__qualname__) # same thing, reached via the instance's type