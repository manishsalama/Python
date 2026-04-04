def rotate_left(lst, n):
    if not lst:
        return lst
    n = n % len(lst) 
    return lst[n:] + lst[:n]

sample_list = [1, 2, 3, 4]
steps = 1
rotated = rotate_left(sample_list, steps)

print(f"Original list: {sample_list}")
print(f"Rotated left by {steps} steps: {rotated}")
print("\n")
