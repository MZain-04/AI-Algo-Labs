text = input("Enter a string: ")

letters = 0
digits = 0

# Check every character
for character in text:

    if character.isalpha():
        letters += 1

    elif character.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)