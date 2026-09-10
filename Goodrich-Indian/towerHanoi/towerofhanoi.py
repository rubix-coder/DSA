def move(disks,source,destination,temp):
    if disks>=1:
        print(f"Disks = {disks} and source = {source}, temp = {temp}, destination = {destination},")

        move(disks-1,source,temp,destination)
        print(f"Disks = {disks} and temp = {temp}, destination = {destination}, source = {source}")

        print(f"Move {source} -> {destination}")

        move(disks-1,temp,destination,source)
        print("\n")

move(3,1,3,2)