class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1


        while i < j:
            m = (i+j)//2
            if nums[m] < nums[j]:
                if j != m:
                    j =m
            elif nums[m] >= nums[j]:
                if i != m+1:
                    i=m+1
        return nums[i]





        