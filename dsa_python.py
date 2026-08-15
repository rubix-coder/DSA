# !/usr/bin/env python3

# """
# Goodrich's 'Data Structures and Algorithms in Python', Chapter 1.5.1: Mutable Parameters

# SECTION 1: MUTABLE PARAMETERS

# 1. Aliasing:
#    - Demonstrates aliasing by scaling elements of a list in place.
#    - Also demonstrates rebinding the parameter to a new list, showing no change to the caller's list.

# 2. Immutability:
#    - Shows that incrementing an integer does not affect the caller's int,
#      demonstrating the same aliasing rule as lists.

# 3. The mutable default argument trap:
#    - Demonstrates a buggy function with a shared default list and shows accumulation.
#    - Corrects the function using a None sentinel to ensure independent results.

# 4. Shallow aliasing in nested structures:
#    - Builds a 3x3 grid with row repetition, showing all rows alias one object.
#    - Demonstrates correct behavior with a comprehension for independent changes.
# """

# def scale_in_place(lst):
#     """
#     Scales every element of the list in place.
#     """
#     for i in range(len(lst)):
#         lst[i] *= 2

# def scale_new_list(lst):
#     """
#     Rebinds the parameter to a new list, showing no change to the caller's list.
#     """
#     lst = [x * 2 for x in lst]

# def increment_immutable(num):
#     """
#     Demonstrates that incrementing an integer does not affect the caller's int,
#     demonstrating the same aliasing rule as lists.
#     """
#     num += 1
#     # This is the same aliasing rule, not a different passing mode.

# def mutable_default_trap():
#     """
#     Demonstrates the mutable default argument trap and how to correct it.
#     """
#     def buggy_function(lst=[]):
#         lst.append(1)
#         return lst

#     print("Buggy function with shared default list:")
#     for _ in range(3):
#         print(buggy_function())

#     print("\nCorrected function using a None sentinel:")
#     def corrected_function(lst=None):
#         if lst is None:
#             lst = []
#         lst.append(1)
#         return lst

#     print("Corrected function results:")
#     for _ in range(3):
#         print(corrected_function())

# def shallow_aliasing():
#     """
#     Demonstrates shallow aliasing in nested structures.
#     """
#     # Correctly demonstrating aliasing
#     row = [0] * 3
#     grid1 = [row] * 3
#     grid1[0][0] = 1

#     print("Grid with shallow aliasing:")
#     for row in grid1:
#         print(row)
#     print(f"Identity comparison of first two rows: {grid1[0] is grid1[1]}")

#     # Correctly demonstrating independent construction
#     correct_grid = [[0] * 3 for _ in range(3)]
#     correct_grid[0][0] = 1

#     print("\nCorrected grid with independently constructed rows:")
#     for row in correct_grid:
#         print(row)
#     print(f"Identity comparison of first two rows: {correct_grid[0] is correct_grid[1]}")


# # SECTION 2: any() AND all()

# def demo_password_rules():
#     """Lesson: Using any and all for complex validation rules."""
#     passwords = ["pass123", "StrongPass123!"]
#     rules = {
#         "min_length": lambda p: len(p) >= 8,
#         "contains_digit": lambda p: any(c.isdigit() for c in p),
#         "contains_uppercase": lambda p: any(c.isupper() for c in p),
#         "contains_lowercase": lambda p: any(c.islower() for c in p),
#         "contains_non_alnum": lambda p: any(not c.isalnum() for c in p)
#     }
    
#     for password in passwords:
#         all_valid = all(rules[rule](password) for rule in rules)
#         failed_rules = [rule for rule in rules if not rules[rule](password)]
        
#         print(f"Password: {password}")
#         print(f"All valid: {all_valid}")
#         print(f"Failed rules: {failed_rules}")

# def demo_service_health():
#     """Lesson: Using any and all to check service health."""
#     services = {
#         "service1": 200,
#         "service2": 503,
#         "service3": 404
#     }
    
#     all_healthy = all(value == 200 for value in services.values())
#     any_down = any(value != 200 for value in services.values())
#     unhealthy_services = [key for key, value in services.items() if value != 200]
    
#     print(f"Services: {services}")
#     print(f"All healthy: {all_healthy}")
#     print(f"Any down: {any_down}")
#     print(f"Unhealthy services: {unhealthy_services}")

# def demo_log_scanning():
#     """Lesson: Using any for efficient log scanning."""
#     alert_substrings = ["error", "fail"]
#     log_lines = [
#         "This is a normal log message.",
#         "An error occurred here.",
#         "Another normal log entry."
#     ]
    
#     alerts_found = [any(substring in line for substring in alert_substrings) for line in log_lines]
    
#     for i, line in enumerate(log_lines):
#         if alerts_found[i]:
#             print(f"Alert found in line {i+1}: {line}")

# def demo_empty_iterables():
#     """Lesson: Understanding vacuous truths with any and all."""
#     empty_list = []
    
#     any_result = any(empty_list)
#     all_result = all(empty_list)
    
#     print(f"Empty list: {empty_list}")
#     print(f"any(): {any_result} (vacuous truth)")
#     print(f"all(): {all_result} (true for empty collection)")

# def demo_short_circuiting():
#     """Lesson: Short-circuit evaluation with any."""
#     def check_value(value):
#         print(f"Checking value: {value}")
#         return value > 2
    
#     result = any(check_value(i) for i in range(1, 6))
    
#     print(f"Result: {result}")

# def demo_generator_vs_list():
#     """Lesson: Comparing generator and list comprehensions with any."""
#     def check_value(value):
#         print(f"Checking value: {value}")
#         return value > 2
    
#     print("Using generator expression:")
#     result_gen = any(check_value(i) for i in range(1, 6))
    
#     print(f"Result: {result_gen}")
    
#     print("\nUsing list comprehension:")
#     result_list = any([check_value(i) for i in range(1, 6)])
    
#     print(f"Result: {result_list}")


# # SECTION 3: id() AND hash()

# def demo_identity_vs_equality():
#     """
#     Lesson 1: Identity versus equality.
#     Equality asks about value and identity asks about which object.
#     """
#     list1 = [1, 2, 3]
#     list2 = [1, 2, 3]
#     print(f"list1 == list2: {list1 == list2}")  # True
#     print(f"list1 is list2: {list1 is list2}")  # False

#     list3 = list1
#     print(f"list1 is list3: {list1 is list3}")  # True


# def demo_address_recycling():
#     """
#     Lesson 2: Address recycling.
#     An identity number is only guaranteed unique among objects that are alive at the same moment.
#     Once an object is discarded its address can be handed to the next object.
#     """
#     print("Discarded phase:")
#     for _ in range(5):
#         obj = object()
#         print(f"id(obj): {id(obj)}")

#     lst = []
#     print("\nRetained phase:")
#     for _ in range(5):
#         obj = object()
#         lst.append(obj)
#         print(f"id(obj): {id(obj)}")
#     print(f"Distinct values seen: {len(set(id(obj) for obj in lst))}")
#     print(f"Total calls made: 5")


# def demo_string_interning():
#     """
#     Lesson 3: String interning.
#     The interpreter deduplicates certain compile-time strings as an optimisation.
#     This is not something a program may rely on, and equality is the only correct test.

#     Part 1: Within a single compilation unit
#     When one chunk of source is compiled in one go, the compiler collapses duplicate equal string constants into a single shared object. Demonstrate this using two side by side literals containing dots, and show that the identity test between them is true. State in the printed label that this sharing happens for any equal constants in the same unit, whatever characters they contain, and is a compiler optimisation rather than interning.
#     """
#     s1 = "he.ll.o"
#     s2 = "he.ll.o"
#     print(f"Part 1: Within a single compilation unit")
#     print(f"s1 == s2: {s1 == s2}")  # True
#     print(f"id(s1) == id(s2): {id(s1) == id(s2)}")  # True

#     """
#     Part 2: Across separate compilation units
#     This is what the interactive prompt does, since it compiles each entered line on its own. Demonstrate it without importing anything by using the two builtins that turn source text into a code object and then execute a code object against a supplied namespace dictionary. Compile two separate one line assignment sources that each bind the same dotted literal, execute each into its own fresh dictionary, and compare the two resulting strings by identity, which is false. Then repeat that whole procedure with a literal whose characters are all letters so that it looks like a Python identifier, and show the identity test is now true.
#     """
#     print(f"\nPart 2: Across separate compilation units")
#     namespace1 = {}
#     exec("s3 = 'he.ll.o'", namespace1)
#     s3 = namespace1['s3']

#     namespace2 = {}
#     exec("s4 = 'he.ll.o'", namespace2)
#     s4 = namespace2['s4']
#     print(f"s3 == s4: {s3 == s4}")  # True
#     print(f"id(s3) == id(s4): {id(s3) == id(s4)}")  # False

#     namespace5 = {}
#     exec("s5 = 'hello'", namespace5)
#     s5 = namespace5['s5']

#     namespace6 = {}
#     exec("s6 = 'hello'", namespace6)
#     s6 = namespace6['s6']
#     print(f"s5 == s6: {s5 == s6}")  # True
#     print(f"id(s5) == id(s6): {id(s5) == id(s6)}")  # True

#     """
#     Conclusion:
#     Strings that look like identifiers are automatically interned so equal ones are shared everywhere in the process, strings containing characters such as dots are not, and therefore two equal strings typed on separate interactive lines may or may not be the same object. End with the practical rule that identity must never be used to compare string values and equality is the only correct test. Every trailing comment that predicts an output value must match what the code actually prints.
#     """


# def demo_hash_contract():
#     """
#     Lesson 4: The hash contract.
#     Objects which compare equal are required to hash equal.
#     """
#     one_int = 1
#     one_float = 1.0
#     one_bool = True

#     print(f"one_int == one_float == one_bool: {one_int == one_float == one_bool}")  # True
#     print(f"hash(one_int) == hash(one_float) == hash(one_bool): {hash(one_int) == hash(one_float) == hash(one_bool)}")  # True

#     my_dict = {one_int: "value"}
#     print(f"my_dict[one_float]: {my_dict[one_float]}")  # value

#     my_set = {one_int, one_float, one_bool}
#     print(f"len(my_set): {len(my_set)}")  # 1


# def demo_hashable_vs_unhashable():
#     """
#     Lesson 5: Hashable versus unhashable.
#     Hashability requires immutability because a hash must not change during an object's lifetime.
#     """
#     my_dict = {}
#     for obj in [1, "hello", (1, 2), frozenset([1, 2]), "he.ll.o", [1, 2], {"a": 1}, {1, 2}]:
#         try:
#             print(f"hash({obj}): {hash(obj)}")
#         except TypeError as e:
#             print(f"Failed to hash {obj}: {e}")

#     try:
#         print(f"hash((1, [2])): {hash((1, [2]))}")
#     except TypeError as e:
#         print(f"Failed to hash (1, [2]): {e}")


# def demo_hash_stability():
#     """
#     Lesson 6: Hash stability.
#     String hashes are deliberately salted with a random seed chosen at interpreter start,
#     so they differ between separate runs of the program even though they are stable within one run.
#     Hashes must therefore never be persisted to a file or database.
#     """
#     fixed_string = "hello"
#     for _ in range(5):
#         print(f"hash({fixed_string}): {hash(fixed_string)}")

#     small_integers = [0, 1, -1, 2**31-1]
#     for i in small_integers:
#         print(f"hash({i}): {hash(i)}")


# def demo_mutating_a_key():
#     """
#     Lesson 7: Mutating a key.
#     A mutation reaching a shared object can silently corrupt a data structure built on top of it.
#     """
#     class Key:
#         def __init__(self, value):
#             self.value = value

#         def __eq__(self, other):
#             return self.value == other.value

#         def __hash__(self):
#             return hash(self.value)

#         def __repr__(self):
#             return f"{self.__class__.__name__}({self.value})"

#     key = Key(1)
#     my_dict = {key: "value"}
#     print(f"my_dict[key]: {my_dict[key]}")  # value

#     key.value = 2
#     try:
#         new_key = Key(2)
#         print(f"my_dict[new_key]: {my_dict[new_key]}")
#     except KeyError as e:
#         print(f"Failed to find value for key with value: {new_key.value}")

#     try:
#         original_key = Key(1)
#         print(f"my_dict[original_key]: {my_dict[original_key]}")
#     except KeyError as e:
#         print(f"Failed to find value for key with value: {original_key.value}")
#     finally:
#         print(f"my_dict contents: {my_dict}")  # {<__main__.Key object at 0x...>: 'value'}

# if __name__ == "__main__":
#     # Demo 1: Aliasing
#     lst1 = [1, 2, 3]
#     lst2 = [1, 2, 3]

#     print("Before scaling in place:", lst1)
#     scale_in_place(lst1)
#     print("After scaling in place:", lst1)  # Should be [2, 4, 6]

#     print("\nBefore scaling with new list:", lst2)
#     scale_new_list(lst2)
#     print("After scaling with new list:", lst2)  # Should still be [1, 2, 3]

#     # Demo 2: Immutability
#     num = 5
#     print(f"Original number: {num}")
#     increment_immutable(num)
#     print(f"After incrementing: {num}")  # Should still be 5

#     # Demo 3: The mutable default argument trap
#     mutable_default_trap()

#     # Demo 4: Row aliasing
#     shallow_aliasing()
#     # Section 2 demonstrations begin
#     demo_password_rules()
#     demo_service_health()
#     demo_log_scanning()
#     demo_empty_iterables()
#     demo_short_circuiting()
#     demo_generator_vs_list()
#     # Section 2 demonstrations begin
#     demo_identity_vs_equality()
#     demo_address_recycling()
#     demo_string_interning()
#     demo_hash_contract()
#     demo_hashable_vs_unhashable()
#     demo_hash_stability()
#     demo_mutating_a_key()



def read_inputs_until_eof():
    lines = []
    
    print("Enter your text (Press Ctrl+D on Linux/Mac or Ctrl+Z on Windows to stop):")
    
    try:
        while True:
            # Continually read a line from standard input
            line = input() 
            lines.append(line)
            
    except EOFError:
        # This block triggers automatically when there is no more input left
        print("\n--- End of File (EOF) Reached ---")
    
    # Process the lines (e.g., printing them in reverse order)
    print("Here are your lines in reverse order:")
    for line in reversed(lines):
        print(line)

# Run the function
if __name__ == '__main__':
    read_inputs_until_eof()