
n = int(input("Enter array size: "))
arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

k = int(input("Enter K: "))

prefix_sum = 0
max_length = 0

prefix_values = [0] * (n + 1)
first_indices = [0] * (n + 1)
count = 0

for i in range(n):
    prefix_sum = prefix_sum + arr[i]

    if prefix_sum == k:
        length = i + 1

        if length > max_length:
            max_length = length

    required = prefix_sum - k
    j = 0

    while j < count:
        if prefix_values[j] == required:
            length = i - first_indices[j]

            if length > max_length:
                max_length = length

            break

        j = j + 1

    j = 0
    found = False

    while j < count:
        if prefix_values[j] == prefix_sum:
            found = True
            break

        j = j + 1

    if not found:
        prefix_values[count] = prefix_sum
        first_indices[count] = i
        count = count + 1

print(max_length)
