n = int(input("Enter number of items: "))

weight = list(map(int, input("Enter weights: ").split()))
profit = list(map(int, input("Enter profits: ").split()))

capacity = int(input("Enter capacity: "))

dp = [0] * (capacity + 1)

for i in range(n):
    for w in range(capacity, weight[i] - 1, -1):
        dp[w] = max(dp[w], profit[i] + dp[w - weight[i]])

print("Maximum Profit =", dp[capacity])