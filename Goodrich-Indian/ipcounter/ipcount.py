class IP():
    def __init__(self,ip="192.168.0.0"):
        self.ip = ip

    def __add__(self,adder):
        parts = [int(x) for x in self.ip.split(".")]
        parts[-1] = (parts[-1]+ adder) %255
        self.ip = ".".join(str(x) for x in parts)
        return IP(self.ip)

    def __str__(self):
        return self.ip
