allowed_names = ["GOKU", "RITHWIK", "SAMI", "MOIZ", "MANISH"]
print(f"Database: {allowed_names}")

name_to_check = input("Enter a name to search for: ")

if name_to_check in allowed_names:
    print(f"Success: {name_to_check} is present in the list.")
else:
    print(f"Error: {name_to_check} was NOT found in the list.")
print("\n")