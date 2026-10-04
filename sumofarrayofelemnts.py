n = int(input("Enter n: "))
arr = list(map(int, input("Enter array elements: ").split()))

total = 0

for i in range(n):
    total += arr[i]

print("Sum =", total)