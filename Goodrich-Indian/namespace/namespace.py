class Test:
    __slots__= "_test"
    def __init__(self):
        print(f"Slots: {self.__slots__}, type: {type(self.__slots__)}")

    def _print(self,text):
        print("hello "+text)


class NestedTest1(Test):
    __slots__="_nest","func"
    def __init__(self): 
        super().__init__()

dictClass = {"A":Test,
             "B":NestedTest1}

for key,val in enumerate(dictClass):
    k = dictClass[val]()
    print(f"Class name : {type(k).__name__}")
    k._print("Jesal\n")