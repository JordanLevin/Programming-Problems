class Solution(object):
    def coinChange(self, coins, amount):
        seen = {}
        if amount == 0:
            return 0
        for coin in coins:
            seen[coin] = 1
        for i in range(1, amount+1):
            if i in seen:
                continue
            result = min([seen[i-c] + 1 if i-c in seen else float('inf') for c in coins])
            seen[i] = result
        if seen[amount] == float('inf'):
            return -1
        return seen[amount]