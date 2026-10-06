numbers = [45, 12, 90, 6, 38, 17, 77, 23, 84]

numbers.sort()

print("Sorted list:", numbers)

target = int(input("Enter number to search: "))

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Number found at index:", mid)
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Number not found")