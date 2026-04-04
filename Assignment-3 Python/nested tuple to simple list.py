nested_tuple = (1, 2, (3, 4), 5)
flat_list = []

for item in nested_tuple:
    if isinstance(item, tuple):
        flat_list.extend(item)
    else:
        flat_list.append(item)

print(f"Nested tuple: {nested_tuple}")
print(f"Flattened list: {flat_list}")
