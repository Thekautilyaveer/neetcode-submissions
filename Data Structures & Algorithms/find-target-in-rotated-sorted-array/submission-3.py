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

        #left = smallest
        if target > nums[-1]:
            i = 0
            j = left-1
            while i <= j:
                mid = (i+j)//2
                if nums[mid] > target:
                    j = mid-1
                elif nums[mid] < target:
                    i = mid+1
                else:
                    return mid
            return -1
        else:
            i = left
            j = len(nums)-1
            while i <= j:
                mid = (i+j)//2
                if nums[mid] > target:
                    j = mid-1
                elif nums[mid] < target:
                    i = mid+1
                else:
                    return mid
            return -1
        


        
            
            
            



        

         