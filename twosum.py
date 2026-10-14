
def two_sum(prices, budget):
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] == budget:
                return [i, j]

    return []


prices = list(map(int, input().split()))
budget = int(input())

print(two_sum(prices, budget))
