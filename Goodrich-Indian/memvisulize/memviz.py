import array
import ctypes
import sys

def print_buffer_map(obj, name="Object"):
    """
    Directly extracts and renders a physical memory map from a contiguous buffer object.
    Supports array.array, bytes, bytearray, and memoryview.
    """
    # 1. Resolve buffer information and dimensions
    if hasattr(obj, 'buffer_info'):
        base_addr, count = obj.buffer_info()
        itemsize = obj.itemsize
        typecode = getattr(obj, 'typecode', 'Raw')
    elif isinstance(obj, (bytes, bytearray, memoryview)):
        # Fallback to standard buffer interface protocols
        try:
            mv = memoryview(obj)
            base_addr = ctypes.addressof(ctypes.c_char.from_buffer(obj))
            count = len(mv)
            itemsize = mv.itemsize
            typecode = mv.format
        except TypeError:
            print(f"[-] Object '{name}' buffer protocol access denied by CPython interpreter.")
            return
    else:
        print(f"[-] Object '{name}' is not a contiguous C-buffer sequence.")
        return

    total_bytes = count * itemsize
    
    # 2. Render terminal frame
    print(f"\n{'='*75}")
    print(f" MEMORY MAP FOR: '{name}' | Type Code: '{typecode}' | Element Size: {itemsize}B")
    print(f"{'='*75}")
    print(f" {'Memory Address':<18} | {'Offset':<8} | {'Raw Bytes (Hex)':<15} | {'Value'}")
    print(f" {'-'*18}-+-{'-'*8}-+-{'-'*15}-+-{'-'*15}")

    # 3. Step through hardware addresses sequentially
    for index in range(count):
        elem_addr = base_addr + (index * itemsize)
        
        # Read the raw physical bytes directly out of CPython memory space
        byte_data = ctypes.string_at(elem_addr, itemsize)
        hex_string = byte_data.hex(' ').upper()
        
        # Unpack raw bytes back into readable Python types for display
        if hasattr(obj, 'typecode'):
            val = obj[index]
        else:
            val = int.from_bytes(byte_data, byteorder=sys.byteorder)

        print(f" 0x{elem_addr:014X} | +0x{index * itemsize:02X}     | {hex_string:<15} | {val}")
        
    print(f" 0x{base_addr + total_bytes:014X} | +0x{total_bytes:02X}     | {'-- '*itemsize:<15} | [Boundary]")
    print(f"{'='*75}\n")

def visualize_memory(name=None):
    """
    A decorator to automatically visualize the returned array buffer of any function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            obj_name = name if name else func.__name__ + "_output"
            print_buffer_map(result, name=obj_name)
            return result
        return wrapper
    return decorator
