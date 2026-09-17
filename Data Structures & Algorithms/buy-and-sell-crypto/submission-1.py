class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        for i in range(len(prices)):
            val = max(prices[i:])-prices[i]
            maxp = max(maxp,val )
        return maxp


            






        