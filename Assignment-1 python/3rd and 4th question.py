
text = "I AM MANISH  REDDY THIS  IS SOME  DOUBLE  SPACES."

print("Original string:", text)

if "  " in text:
    print("\nStatus: Double spaces detected! Fixing now...")

    text = text.replace("  ", " ")
    
    print("Fixed string:   ", text)

else:
    print("\nStatus: No double spaces found. The string is GOOD!")