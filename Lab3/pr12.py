# Take comma-separated binary numbers
data = input("Enter binary numbers: ")

# Split the numbers
numbers = data.split(",")

result = []

# Check each binary number
for binary in numbers:

    # Convert binary to decimal
    decimal = int(binary, 2)

    # Check if it is divisible by 5
    if decimal % 5 == 0:
        result.append(binary)

# Print the result
print(",".join(result))