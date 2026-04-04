comment = input("Enter a comment to check for spam: ")
comment_lower = comment.lower()

spam_detected = False

if "make a lot of money" in comment_lower:
    spam_detected = True
elif "buy now" in comment_lower:
    spam_detected = True
elif "subscribe this" in comment_lower:
    spam_detected = True
elif "click this" in comment_lower:
    spam_detected = True

if spam_detected:
    print("Warning: This YOUR comment is flagged as SPAM.")
else:
    print("This comment looks SAFE.")
print("\n")