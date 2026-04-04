my_tuple = (10, 20, 30)
print("Original tuple:", my_tuple)
print("Attempting to change the first element (index 0) to 99...")

try:
    my_tuple[0] = 99 
except TypeError as e:
    print("Tuples are static:", e)
    print("Tuples cannot be changed.")
print("\n")