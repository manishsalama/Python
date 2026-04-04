print("Enter marks for 3 subjects (out of 100):")
sub1 = float(input("Subject 1 marks: "))
sub2 = float(input("Subject 2 marks: "))
sub3 = float(input("Subject 3 marks: "))

total_percentage = (sub1 + sub2 + sub3) / 3

if total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print(f"Result: YOU ARE PASSED CONGORATS! (Total Percentage: {total_percentage:.2f}%)")
else:
    print(f"Result: YOU ARE FAILED.U HAVE BACKLOGS NOW. (Total Percentage: {total_percentage:.2f}%)")
print("\n")