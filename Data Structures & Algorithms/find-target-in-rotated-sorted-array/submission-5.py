class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        mid = 0
        while nums[left] > nums[right]:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid


        if target > nums[-1]:
            i, j = 0, left - 1
        else:
            i, j = left, len(nums) - 1

        while i <= j:
            mid = (i+j)//2
            if nums[mid] > target:
                j = mid-1
            elif nums[mid] < target:
                i = mid+1
            else:
                return mid
        return -1

        


        
            
            
            



        

         