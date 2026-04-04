int_tuple = (2, 4, 3, 5, 7, 1, 8, 0)
print(f"Tuple available: {int_tuple}")

target = int(input("Enter a target number: "))
pairs = []
for i in range(len(int_tuple)):
    for j in range(i + 1, len(int_tuple)):
        if int_tuple[i] + int_tuple[j] == target:
            pairs.append((int_tuple[i], int_tuple[j]))

print(f"Pairs that sum up to {target}: {pairs}")
print("\n")
