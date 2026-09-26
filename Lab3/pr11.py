# Keep taking lines until the user enters a blank line

while True:
    line = input()

    # Stop if the line is blank
    if line == "":
        break

    # Convert the line to lowercase
    print(line.lower())