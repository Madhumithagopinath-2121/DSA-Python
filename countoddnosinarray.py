n = int(input("Enter n: "))
arr = list(map(int, input("Enter array elements: ").split()))

count = 0

for i in range(n):
    if arr[i] % 2 != 0:
        count += 1

print("Count of odd numbers =", count)