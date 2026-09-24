coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

dp = [999] * (amount + 1)
dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == 999:
    print("Change not possible")
else:
    print("Minimum coins =", dp[amount])