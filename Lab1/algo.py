#1 algorithm
arr = [1,2,6,4,5]
n = 9

for i in range(len(arr)):
    if arr[i] == n:
        print("Value found")
print("value not found")

#2 algorithm
arr2 = [6,7,8,9,10]
arr3 = [6,3,8,5,12]
for i in range(len(arr2)):
    if arr2[i] == n:
        print("Value found in array 2")
for i in range(len(arr3)):
    if arr3[i] == n:
        print("Value found in array 3")

#3 algorithm
for i in range(len(arr2)):
    for j in range(len(arr3)):
        if arr2[i] == arr3[j]:
            print("Value are same in both arrays")
print("value not found")    
   
               