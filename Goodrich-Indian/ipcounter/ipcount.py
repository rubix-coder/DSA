class IP():
    def __init__(self):
        self.ip = "192.168.1.1"

    def __add__(self):
        self.ender = self.ip.split(".")[-1]
        self.ender+=1
        return self
        
    