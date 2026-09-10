import sys
# import ctypes

# data = []
# n = 26

# def getComponentValues(data):
# # 2. Get the starting memory address of the list object
#     address = id(data)

#     # 3. Read the 8-byte chunks directly from that memory location
#     # (Offsets are in steps of 8 bytes because it's a 64-bit system)
#     ob_refcnt = ctypes.c_ssize_t.from_address(address + 0).value
#     ob_type   = ctypes.c_ssize_t.from_address(address + 8).value
#     ob_size   = ctypes.c_ssize_t.from_address(address + 16).value
#     ob_item   = ctypes.c_ssize_t.from_address(address + 24).value
#     allocated = ctypes.c_ssize_t.from_address(address + 32).value

#     # 4. Display the values inside the fields
#     print(f"=== PyListObject Fields at Address: {hex(address)} ===")
#     print(f"1. ob_refcnt : {ob_refcnt}         <- How many variables point to this list")
#     print(f"2. ob_type   : {hex(ob_type)} <- Memory address of the <class 'list'>")
#     print(f"3. ob_size   : {ob_size}         <- Current number of items (0 means empty)")
#     print(f"4. ob_item   : {hex(ob_item)}        <- Pointer to item array (0x0 or NULL when empty)")
#     print(f"5. allocated : {allocated}         <- Total reserved slots in memory")


# for k in range(n):
#     a = len(data)
#     b = sys.getsizeof(data)
#     print(f"Length -> {a}; size in bytes -> {b}")
#     getComponentValues(data)
#     data.append(None)


# for i in range(0,5):
#     print(f"2^(i-1) -> {pow(2,i-1)}")
#     print(f"(2^i)-1 -> {pow(2,i)-1}")

from time import time

start = time()
for i in range(1,1000):
    d = [0]*i
    print(sys.getsizeof(d))
    elapsed = time()-start
    print(elapsed)