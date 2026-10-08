class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res= nums[0]
        big, small = nums[0], nums[0]
        for i in range(1, len(nums)):

            big, small = max(nums[i], nums[i]*big, nums[i]*small), min(nums[i], nums[i]*big, nums[i]*small)
            res = max(big, res)
         
            
        return res


