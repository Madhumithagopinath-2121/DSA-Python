
numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0]
second = None

for i in range(1, len(numbers)):
    if numbers[i] > largest:
        second = largest
        largest = numbers[i]
    elif numbers[i] < largest:
        if second is None or numbers[i] > second:
            second = numbers[i]

if second is None:
    print("No second largest distinct number")
else:
    print("Second largest:", second)
