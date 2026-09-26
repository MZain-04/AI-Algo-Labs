# First two Fibonacci numbers

a = 0
b = 1

# Continue while the number is less than or equal to 50
while a <= 50:
    print(a, end=" ")

    # Find the next Fibonacci number
    a, b = b, a + b

#(b)part

# Loop from 1 to 50
for number in range(1, 51):

    # Check both 3 and 5 first
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)
