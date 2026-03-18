

numbers = [10,10,20,20,30]
unique = []

for num in numbers:
    if  num not in unique:
        unique.append(num)

print("List without duplicates:", unique)