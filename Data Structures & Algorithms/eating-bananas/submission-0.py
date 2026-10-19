import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_val = max(piles)

        left = 1
        right = max_val
        visited = set()
        slowest = float('inf')
        while left<= right:
            mid = (left+right)//2

            
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            if hours > h:
                left = mid+1
            elif hours <= h:
                right = mid-1
                slowest = min(slowest, mid) 


        return slowest
        
'''(1,2,3,4)
left = 1
right = 4
mid = 2
hours = 1+1+2+2 = 6

left = 1
right = 1
mid = 1
hours = 1+4+3+2 = 10

------------
piles=[25,10,23,4]
h=4

left = 1
right = 25
mid = 13
hours= 2+ 1+2+1 = 6

left = 14
right = 25
mid = 20
hours = 2+1+2+1 = 6

left = 21
right = 25'''




