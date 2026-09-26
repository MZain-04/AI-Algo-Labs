#Find numbers b/w 1500 and 2700
#Which are divisible by both 7 and 5

for number in range(1500,2701):
    if number % 7 == 0 and number % 5 == 0:
        print(number)
        