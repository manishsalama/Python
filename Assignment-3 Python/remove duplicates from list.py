original_list = [4, 2, 4, 1, 3, 2, 5, 1]
Non duplicate list = []

for item in original_list:
    # Only add the item if we haven't seen it yet
    if item not in Non duplicate list :
        Non duplicate list.append(item)

print(f"Original list: {original_list}")
print(f"List with unique elements: {Non duplicate list}")
print("\n")