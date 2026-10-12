
target = int(input("Enter target: "))
n = int(input("Enter array size: "))

nums = [0] * n

for i in range(n):
    nums[i] = int(input("Enter element: "))

left = 0
current_sum = 0
min_length = n + 1

for right in range(n):
    current_sum = current_sum + nums[right]

    while current_sum >= target:
        length = right - left + 1

        if length < min_length:
            min_length = length

        current_sum = current_sum - nums[left]
        left = left + 1

if min_length == n + 1:
    print(0)
else:
    print(min_length)
