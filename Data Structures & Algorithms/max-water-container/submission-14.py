class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxvalue = 0

        while left < right:
            maxvalue = max(maxvalue, ((right-left) * min(heights[left], heights[right])))
            if heights[left]< heights[right]:
                left +=1
            elif heights[right] < heights[left]:
                right -=1
            else:
                left+=1
        return maxvalue