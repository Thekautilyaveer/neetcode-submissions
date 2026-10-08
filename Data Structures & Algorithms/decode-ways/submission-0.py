class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1 for _ in range(len(s)+1)]
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]

            res = dfs(i + 1)  # take one digit
            
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i + 2)  # take two digits

            dp[i] = res
            return dp[i]

        return dfs(0)