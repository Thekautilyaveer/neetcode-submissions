class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robMax(index, end):

            if index >= end:
                return 0
            if dp[index] != -1:
                return dp[index]

            rob = nums[index]+ robMax(index+2, end)
            skip = robMax(index+1, end)
            dp[index] = max(rob, skip)
            return dp[index]
        dp = [-1 for _ in range(len(nums)+1)]
        first = robMax(0, len(nums)-1)
        dp = [-1 for _ in range(len(nums)+1)]
        second = robMax(1, len(nums))

        return max(first, second)



        