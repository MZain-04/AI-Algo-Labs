# Count Even and Odd numbers

numbers = (1,2,3,4,5,6,7,8)
even = 0
odd = 0

# Check every number

for number in numbers:
    if number % 2 == 0:
        even +=1
    else: 
        odd +=1

print("Number of even numbers:", even)            
print("Number of odd numbers:", odd)            
