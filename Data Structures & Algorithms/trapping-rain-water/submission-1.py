class Solution:
    def trap(self, height: List[int]) -> int:
        water =0
        max_left =height[0]
        max_right = height[len(height)-1]
        left = 0
        right = len(height)-1

        while left < right:
            if height[left]<height[right]:
                max_left = max(max_left, height[left])
                water += max_left - height[left]
                left+=1
            else:
                max_right = max(max_right, height[right])
                water+= max_right-height[right]
                right-=1


        return water



        




        