print("Enter four numbers:")
n1 = float(input("Number 1: "))
n2 = float(input("Number 2: "))
n3 = float(input("Number 3: "))
n4 = float(input("Number 4: "))

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    greatest = n1
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    greatest = n2
elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    greatest = n3
else:
    greatest = n4

print(f"The greatest number entered is: {greatest}")