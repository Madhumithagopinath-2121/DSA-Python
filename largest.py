
numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]

print("Largest number:", largest)
