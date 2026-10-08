class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(i, amount):
            if amount == 0:
                return 0


            if i >= len(coins) or amount < 0:
                return float('inf')

            if (i, amount) in dp:
                return dp[i, amount]

            include = 1 + dfs(i, amount-coins[i])
            exclude = 0+ dfs(i+1, amount)

            dp[i, amount]= min(include, exclude)
            return dp[i, amount] 

        res = dfs(0, amount)
        return -1 if res == float('inf') else res

            


