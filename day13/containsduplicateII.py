
def containsNearbyDuplicate(nums, k):
    seen = {}

    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True

        seen[num] = i

    return False


nums = list(map(int, input().split()))
k = int(input())

print(containsNearbyDuplicate(nums, k))
