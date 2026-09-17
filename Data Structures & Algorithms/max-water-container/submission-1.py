class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma = 0
        f, b = 0, len(heights)-1
        while f<b:
            area = (min(heights[f], heights[b])*(b-f))
            ma = max(ma, area)
            if heights[f]<heights[b] or heights[f]== heights[b]:
                f+=1
            elif heights[b]<heights[f]:
                b-=1
            

        
        return ma

        