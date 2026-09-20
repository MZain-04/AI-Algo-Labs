#for in loop
#Example:1
print("List iteration")
List = ["Red", "Green", "Yellow"]
for i in List:
    print(i)

#Example:2
#iterating over a tuple #tuple or immutable means not be changed
print("\nTuple iteration")    
t = ("geeks","for","geeks")
for i in t:
    print(i)

#Example:3
#Iterating over a string
print("\nString Iteration")    
s = "Geeks"
for i in s:
    print(i)

#--------- Iterating by index of sequence
inde = ["geeks","for","geeks"]    
for index in range(len(inde)):
    print(inde[index])

#--------- Loop Control Statement    
#Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
          continue  #continue return the control to the begining of the loop
    print('Current Letter:', letter)

#Break Statement:
for mt in 'Hello buds':
    if mt == 'e' or mt == 's':
          break #break brings control out of the loop
    print('Current Letter:',mt)