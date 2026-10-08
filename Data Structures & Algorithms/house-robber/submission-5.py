class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums)+1)]
        def maxMoney(index):
            if index >= len(nums):
                return 0
            if dp[index] != -1:
                return dp[index]

            rob = nums[index]+maxMoney(index+2)
            skip = maxMoney(index+1)
            dp[index]= max(rob, skip)
            return dp[index]

        return maxMoney(0)
        