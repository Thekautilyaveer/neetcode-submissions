class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(len(cost)+1)]
        def findMin(index):

            if index == len(cost)-1:
                return cost[-1]
            if index >= len(cost):
                return 0
            if dp[index] != -1:
                return dp[index]


            left = findMin(index+1) + cost[index]
            right = findMin(index+2) + cost[index]

            dp[index] = min(left, right)
            return dp[index]

        return min(findMin(0), findMin(1))


            






        