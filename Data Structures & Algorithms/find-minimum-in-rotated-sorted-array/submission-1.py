class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        if nums[i]< nums[j]:
            return nums[i]
        else:
            while (j-i)>1:
                mid = (i+j)//2
                if nums[mid] > nums[i]:
                    if i != mid:
                        i = mid

                elif nums[mid] < nums[i]:
                    if j != mid:
                        j = mid
            return min(nums[i], nums[j])

                





        