from ipcount import IP


if __name__=="__main__":
    ip = IP()
    for _ in range(10):
        ip+=1
        print(ip)