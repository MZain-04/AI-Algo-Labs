# Take rows and columns from the user
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

array = []

# Create each row
for i in range(rows):
    row = []

    # Create each column
    for j in range(columns):
        row.append(i * j)

    array.append(row)

print(array)