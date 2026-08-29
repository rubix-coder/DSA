# class _:
#     def __init__(self,text):
#         self.__txt = text

#     def __name__(self):
#         return str("patel")

#     def __str__(self):
#         " ".join(self.__txt)
#         return str(_.__name__ + " ".join(self.__txt))

# jp  = _("jesal")
# print(jp)
# print(_.__qualname__)        # the class's actual dotted name
# print(type(jp).__qualname__) # same thing, reached via the instance's type

import copy 

class Pallete:
    def __init__(self,red ='a'):
        self.redcol=red
        self.red ='0xFF0000'
        self.green = '0x00FF00'
        self.blue = '0x0000FF'
    def update_hex(self,color,hexval):
        setattr(self,color,hexval)
        print(setattr(self,color,hexval))
        return getattr(self,color)
    
    def __str__(self):
        return f"{self.red,self.green,self.blue}"


warmtones = Pallete()
print(warmtones)
p = copy.deepcopy(warmtones)
print(f"deepcopy of warmtones: {p}")

warmtones.update_hex(color="red",hexval='0x124567')
print(warmtones)
print(p)

class change:
    def __init__(self,x, y, z):
        self.jesal = x + y + z

x = change(1,2,3)
y = getattr(x,'jesal')
setattr(x,'jesal',y+1)
print(x.jesal)