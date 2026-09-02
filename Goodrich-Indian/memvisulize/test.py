import array
from memviz import visualize_memory, print_buffer_map

# --- METHOD 1: Using it as a Decorator ---
@visualize_memory(name="Sensor Data Buffer")
def fetch_telemetry():
    # Constructing a standard signed 4-byte integer array ('i')
    return array.array('i', [0])

# Triggering the function executes the print layout automatically
data_array = fetch_telemetry()


# --- METHOD 2: Direct Inline Execution ---
# Works perfectly for tracking mutations or manual inspection halfway down a script
my_bytes = bytearray([0])
print_buffer_map(my_bytes, name="Mutated Byte Array")
