class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]


        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue


                if i-1 >= 0:
                    up = dp[i-1][j]
                else: 
                    up = 0
                if j-1 >= 0:
                    left = dp[i][j-1]
                else:
                    left = 0
                dp[i][j] = up+left

        return dp[m-1][n-1]

        