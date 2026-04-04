marks = []
print("Please enter the marks of 5 students:")
for i in range(5):
    mark = float(input(f"Marks for Student {i+1}: "))
    marks.append(mark)
marks.sort()
print("Marks in sorted order:", marks)
print("\n")