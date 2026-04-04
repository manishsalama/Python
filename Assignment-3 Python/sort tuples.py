tuples_list = [(1, 5), (9, 2), (4, 8), (3, 1)]

tuples_list.sort(key=lambda x: x[-1])

print(f"Sorted by last element: {tuples_list}")
print("\n")
