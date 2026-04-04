name = input("Enter your name: ")
date = input("Enter date: ")

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)