


numbers = [10,20,30,40,30,60]

largest = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("largest",largest)
print("Second largest:", second)