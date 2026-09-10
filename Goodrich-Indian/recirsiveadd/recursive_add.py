
def addi(n):
    total = n
    if n >= 1:
        total+=addi(n-1)
    return total
    

print(addi(5))