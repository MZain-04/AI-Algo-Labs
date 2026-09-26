password = input("Enter your password: ")

lowercase = False
uppercase = False
number = False
special = False

# Check every character in the password
for character in password:

    if character.islower():
        lowercase = True

    elif character.isupper():
        uppercase = True

    elif character.isdigit():
        number = True

    elif character in "$#@":
        special = True


# Check all password requirements
if (6 <= len(password) <= 16
        and lowercase
        and uppercase
        and number
        and special):

    print("Valid password")

else:
    print("Invalid password")